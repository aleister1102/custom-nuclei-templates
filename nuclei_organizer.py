#!/usr/bin/env python3
"""
Nuclei Template Organizer
Phân loại nuclei templates theo công nghệ và kiểu tấn công
Xóa template trùng lặp và những template không thuộc web pentest
"""

import os
import sys
import yaml
import hashlib
import shutil
import re
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Set, Tuple, Optional

class NucleiOrganizer:
    def __init__(self, source_dirs: List[str], target_dir: str = "organized-folder"):
        self.source_dirs = source_dirs
        self.target_dir = Path(target_dir)
        self.target_dir.mkdir(exist_ok=True)
        
        # Tracking
        self.processed_files = 0
        self.duplicate_files = 0
        self.skipped_files = 0
        self.moved_files = 0
        self.parse_errors = 0
        self.non_web_templates = 0
        self.script_templates = 0
        self.missing_files = 0
        self.file_hashes: Set[str] = set()
        self.categorized_files: Dict[str, List[Dict]] = defaultdict(list)
        self.reports: Dict[str, Dict] = defaultdict(dict)
        
        # Web pentest related keywords
        self.web_keywords = {
            'technologies': {
                'apache', 'nginx', 'iis', 'tomcat', 'jboss', 'weblogic', 'websphere',
                'php', 'asp', 'aspnet', 'jsp', 'python', 'nodejs', 'ruby', 'perl',
                'wordpress', 'drupal', 'joomla', 'magento', 'prestashop', 'opencart',
                'mysql', 'postgresql', 'mongodb', 'redis', 'elasticsearch', 'oracle',
                'spring', 'struts', 'hibernate', 'django', 'flask', 'laravel', 'symfony',
                'react', 'angular', 'vue', 'jquery', 'bootstrap', 'ajax',
                'jenkins', 'gitlab', 'github', 'bitbucket', 'sonarqube',
                'docker', 'kubernetes', 'grafana', 'prometheus', 'kibana',
                'confluence', 'jira', 'sharepoint', 'exchange', 'outlook',
                'phpmyadmin', 'adminer', 'webmin', 'cpanel', 'plesk',
                'apache-httpd', 'apache-tomcat', 'microsoft-iis', 'lighttpd', 'caddy'
            },
            'attack_types': {
                'sqli', 'sql-injection', 'xss', 'cross-site-scripting', 'csrf', 'ssrf',
                'lfi', 'rfi', 'file-inclusion', 'path-traversal', 'directory-traversal',
                'xxe', 'xml-external-entity', 'deserialization', 'template-injection',
                'command-injection', 'code-injection', 'ldap-injection', 'xpath-injection',
                'file-upload', 'unrestricted-file-upload', 'weak-authentication',
                'broken-authentication', 'session-fixation', 'privilege-escalation',
                'information-disclosure', 'sensitive-data-exposure', 'security-misconfiguration',
                'broken-access-control', 'cors', 'clickjacking', 'open-redirect',
                'http-smuggling', 'request-smuggling', 'cache-poisoning', 'host-header-injection'
            }
        }
        
        # Non-web pentest patterns (to exclude)
        self.non_web_patterns = {
            'network', 'smb', 'ssh', 'ftp', 'telnet', 'snmp', 'ldap', 'dns', 'ntp',
            'rdp', 'vnc', 'database-only', 'infrastructure', 'iot-device', 'scada',
            'bluetooth', 'wifi', 'wireless', 'mobile-app', 'android', 'ios',
            'windows-service', 'linux-service', 'binary-analysis', 'malware'
        }

    def get_file_hash(self, file_path: Path) -> str:
        """Tính hash của file để check trùng lặp"""
        # Check if file exists first
        if not file_path.exists():
            return ""
            
        hasher = hashlib.md5()
        try:
            with open(file_path, 'rb') as f:
                buf = f.read()
                hasher.update(buf)
            return hasher.hexdigest()
        except (FileNotFoundError, PermissionError, OSError) as e:
            # File was deleted or inaccessible during processing
            return ""
        except Exception as e:
            if hasattr(self, 'parse_errors') and self.parse_errors <= 5:
                print(f"⚠️  Hash error in {file_path.name}: {str(e)[:60]}...")
            return ""

    def parse_yaml_template(self, file_path: Path) -> Optional[Dict]:
        """Parse YAML template và extract thông tin"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                raw_content = f.read()
            
            # Fix common YAML issues: replace tabs with spaces
            fixed_content = raw_content.replace('\t', '  ')
            
            # Try to parse the fixed content
            content = yaml.safe_load(fixed_content)
            
            if not isinstance(content, dict) or 'info' not in content:
                return None
                
            return content
        except yaml.YAMLError as e:
            self.parse_errors += 1
            # Only show YAML errors for debugging, don't spam console
            if self.parse_errors <= 5 or self.parse_errors % 100 == 0:
                print(f"⚠️  YAML error #{self.parse_errors} in {file_path.name}: Tab characters fixed, retrying...")
            return None
        except Exception as e:
            self.parse_errors += 1
            if self.parse_errors <= 5 or self.parse_errors % 100 == 0:
                print(f"⚠️  Parse error #{self.parse_errors} in {file_path.name}: {str(e)[:80]}...")
            return None

    def is_web_pentest_template(self, template_data: Dict, file_path: Path) -> bool:
        """Kiểm tra xem template có thuộc web pentest không"""
        # Check for script execution or payload requirements
        if self.has_script_execution(template_data):
            return False
            
        # Get all text content for analysis
        content_text = str(template_data).lower()
        file_name = file_path.name.lower()
        
        # Check for non-web patterns
        for pattern in self.non_web_patterns:
            if pattern in content_text or pattern in file_name:
                return False
        
        # Check for web-related patterns
        web_indicators = 0
        
        # Check tags
        tags = template_data.get('info', {}).get('tags', [])
        if isinstance(tags, str):
            tags = [tags]
        
        for tag in tags:
            tag_lower = str(tag).lower()
            if any(keyword in tag_lower for keyword in self.web_keywords['technologies']):
                web_indicators += 2
            if any(keyword in tag_lower for keyword in self.web_keywords['attack_types']):
                web_indicators += 1
        
        # Check HTTP requests
        if 'http' in template_data or 'requests' in template_data:
            web_indicators += 3
            
        # Check for web-specific paths/endpoints
        web_paths = ['/admin', '/login', '/api/', '/wp-', '/cms', '.php', '.asp', '.jsp']
        if any(path in content_text for path in web_paths):
            web_indicators += 1
            
        # Check CVE patterns for web vulnerabilities
        if 'cve' in content_text and any(web_term in content_text for web_term in ['web', 'http', 'browser', 'server']):
            web_indicators += 1
            
        return web_indicators >= 2

    def has_script_execution(self, template_data: Dict) -> bool:
        """Kiểm tra xem template có yêu cầu thực thi script không"""
        content_text = str(template_data).lower()
        
        script_patterns = [
            'code:', 'script:', 'payload:', 'execute:', 'shell:',
            'python:', 'bash:', 'powershell:', 'cmd:', 'system(',
            'exec(', 'eval(', 'subprocess', 'os.system'
        ]
        
        return any(pattern in content_text for pattern in script_patterns)

    def categorize_template(self, template_data: Dict, file_path: Path) -> str:
        """Phân loại template theo công nghệ hoặc kiểu tấn công"""
        info = template_data.get('info', {})
        tags = info.get('tags', [])
        name = info.get('name', '').lower()
        
        if isinstance(tags, str):
            tags = [tags]
        
        # Convert all tags to lowercase
        tags_lower = [str(tag).lower() for tag in tags]
        
        # Priority 1: Technology-based categorization
        for tech in self.web_keywords['technologies']:
            if any(tech in tag for tag in tags_lower) or tech in name or tech in file_path.name.lower():
                return f"technology-{tech}"
        
        # Priority 2: Attack type categorization
        for attack in self.web_keywords['attack_types']:
            if any(attack in tag for tag in tags_lower) or attack in name:
                return f"attack-{attack}"
        
        # Priority 3: CVE categorization
        if any('cve' in tag for tag in tags_lower) or 'cve-' in name:
            return "cve-vulnerabilities"
        
        # Priority 4: Generic categorization
        if any('info' in tag for tag in tags_lower) or 'info' in info.get('severity', ''):
            return "information-gathering"
        
        if any('config' in tag for tag in tags_lower) or 'config' in name:
            return "configuration-issues"
        
        # Default category
        return "miscellaneous"

    def organize_templates(self):
        """Phân loại tất cả templates"""
        print("🔍 Scanning for nuclei templates...")
        
        yaml_files = []
        for source_dir in self.source_dirs:
            source_path = Path(source_dir)
            if source_path.exists():
                yaml_candidates = list(source_path.rglob("*.yaml")) + list(source_path.rglob("*.yml"))
                # Filter out non-existent files (e.g., deleted files still in git index)
                yaml_files.extend([f for f in yaml_candidates if f.exists()])
        
        print(f"📁 Found {len(yaml_files)} YAML files (existing only)")
        
        for file_path in yaml_files:
            self.processed_files += 1
            if self.processed_files % 100 == 0:
                print(f"📊 Processed {self.processed_files}/{len(yaml_files)} files...")
            
            # Check for duplicates
            file_hash = self.get_file_hash(file_path)
            if not file_hash:
                if not file_path.exists():
                    self.missing_files += 1
                self.skipped_files += 1
                continue
                
            if file_hash in self.file_hashes:
                self.duplicate_files += 1
                continue
                
            self.file_hashes.add(file_hash)
            
            # Parse template
            template_data = self.parse_yaml_template(file_path)
            if not template_data:
                self.skipped_files += 1
                continue
            
            # Check for script execution first
            if self.has_script_execution(template_data):
                self.script_templates += 1
                self.skipped_files += 1
                continue
            
            # Check if it's web pentest related
            if not self.is_web_pentest_template(template_data, file_path):
                self.non_web_templates += 1
                self.skipped_files += 1
                continue
            
            # Categorize
            category = self.categorize_template(template_data, file_path)
            
            # Create category directory
            category_dir = self.target_dir / category
            category_dir.mkdir(exist_ok=True)
            
            # Move file
            target_file = category_dir / file_path.name
            
            # Handle duplicate names in same category
            counter = 1
            while target_file.exists():
                name_parts = file_path.name.rsplit('.', 1)
                if len(name_parts) == 2:
                    target_file = category_dir / f"{name_parts[0]}_{counter}.{name_parts[1]}"
                else:
                    target_file = category_dir / f"{file_path.name}_{counter}"
                counter += 1
            
            try:
                # Double-check file still exists before moving
                if not file_path.exists():
                    self.missing_files += 1
                    self.skipped_files += 1
                    continue
                    
                shutil.move(str(file_path), str(target_file))
                self.moved_files += 1
                
                # Track for reporting
                file_info = {
                    'name': target_file.name,
                    'original_path': str(file_path),
                    'info': template_data.get('info', {}),
                    'hash': file_hash
                }
                self.categorized_files[category].append(file_info)
                
            except (FileNotFoundError, PermissionError) as e:
                # File was deleted or not accessible
                self.missing_files += 1
                self.skipped_files += 1
            except Exception as e:
                print(f"❌ Error moving {file_path.name}: {str(e)[:60]}...")
                self.skipped_files += 1

    def generate_reports(self):
        """Tạo báo cáo markdown cho từng category"""
        print("📝 Generating reports...")
        
        # Overall report
        overall_report = f"""# Nuclei Templates Organization Report

## Summary
- **Total files processed**: {self.processed_files}
- **Files moved**: {self.moved_files}
- **Duplicate files removed**: {self.duplicate_files}
- **Files skipped**: {self.skipped_files}
  - Parse errors (invalid YAML): {self.parse_errors}
  - Script/payload templates: {self.script_templates}
  - Non-web pentest templates: {self.non_web_templates}
  - Missing/deleted files: {self.missing_files}
  - Other issues: {self.skipped_files - self.parse_errors - self.script_templates - self.non_web_templates - self.missing_files}
- **Categories created**: {len(self.categorized_files)}

## Categories Overview
"""
        
        for category, files in self.categorized_files.items():
            overall_report += f"- **{category}**: {len(files)} templates\n"
        
        # Save overall report
        with open(self.target_dir / "README.md", 'w', encoding='utf-8') as f:
            f.write(overall_report)
        
        # Individual category reports
        for category, files in self.categorized_files.items():
            category_report = f"""# {category.replace('-', ' ').title()} Templates

## Summary
- **Total templates**: {len(files)}
- **Category**: {category}

## Templates List

"""
            
            # Group by severity
            severity_groups = defaultdict(list)
            for file_info in files:
                severity = file_info['info'].get('severity', 'unknown')
                severity_groups[severity].append(file_info)
            
            for severity in ['critical', 'high', 'medium', 'low', 'info', 'unknown']:
                if severity in severity_groups:
                    category_report += f"### {severity.title()} Severity ({len(severity_groups[severity])} templates)\n\n"
                    
                    for file_info in severity_groups[severity]:
                        name = file_info['info'].get('name', file_info['name'])
                        author = file_info['info'].get('author', 'unknown')
                        description = file_info['info'].get('description', 'No description')
                        tags = file_info['info'].get('tags', [])
                        
                        # Fix tags formatting - handle both string and list
                        if isinstance(tags, str):
                            tags_str = tags
                        elif isinstance(tags, list):
                            tags_str = ', '.join(str(tag) for tag in tags)
                        else:
                            tags_str = 'None'
                        
                        if isinstance(description, str) and len(description) > 200:
                            description = description[:200] + "..."
                        
                        category_report += f"""#### {name}
- **File**: `{file_info['name']}`
- **Author**: {author}
- **Tags**: {tags_str}
- **Description**: {description}

"""
            
            # Save category report
            category_file = self.target_dir / f"{category}_report.md"
            with open(category_file, 'w', encoding='utf-8') as f:
                f.write(category_report)

    def print_summary(self):
        """In tóm tắt kết quả"""
        print("\n" + "="*60)
        print("🎉 ORGANIZATION COMPLETED!")
        print("="*60)
        print(f"📊 Total files processed: {self.processed_files}")
        print(f"✅ Files successfully moved: {self.moved_files}")
        print(f"🔄 Duplicate files removed: {self.duplicate_files}")
        print(f"⏭️  Files skipped: {self.skipped_files}")
        print(f"   • Parse errors (tab chars, invalid YAML): {self.parse_errors}")
        print(f"   • Script/payload templates: {self.script_templates}")
        print(f"   • Non-web pentest templates: {self.non_web_templates}")
        print(f"   • Missing/deleted files: {self.missing_files}")
        print(f"   • Other issues: {self.skipped_files - self.parse_errors - self.script_templates - self.non_web_templates - self.missing_files}")
        print(f"📁 Categories created: {len(self.categorized_files)}")
        print(f"📝 Target directory: {self.target_dir}")
        
        print("\n📋 Categories breakdown:")
        for category, files in sorted(self.categorized_files.items()):
            print(f"   {category}: {len(files)} templates")
        
        print(f"\n📄 Reports generated in: {self.target_dir}")


def main():
    print("🚀 Nuclei Template Organizer")
    print("="*40)
    
    # Get all subdirectories as source directories
    current_dir = Path('.')
    source_dirs = [str(d) for d in current_dir.iterdir() 
                   if d.is_dir() and not d.name.startswith('.') 
                   and d.name != 'organized-folder']
    
    if not source_dirs:
        print("❌ No source directories found!")
        return
    
    print(f"📂 Source directories found: {len(source_dirs)}")
    for dir_name in source_dirs[:10]:  # Show first 10
        print(f"   - {dir_name}")
    if len(source_dirs) > 10:
        print(f"   ... and {len(source_dirs) - 10} more")
    
    # Initialize organizer
    organizer = NucleiOrganizer(source_dirs)
    
    try:
        # Organize templates
        organizer.organize_templates()
        
        # Generate reports
        organizer.generate_reports()
        
        # Print summary
        organizer.print_summary()
        
    except KeyboardInterrupt:
        print("\n⚠️  Process interrupted by user")
    except Exception as e:
        print(f"\n❌ Error during organization: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main() 