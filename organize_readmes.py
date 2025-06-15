#!/usr/bin/env python3
"""
README Organization Script
Move category reports to their respective directories and update root README
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List
import re

class ReadmeOrganizer:
    def __init__(self, target_folder: str = "."):
        self.target_folder = Path(target_folder)
        self.moved_reports = []
        self.failed_moves = []
        self.category_info = {}
        
    def scan_reports_and_categories(self):
        """Scan for report files and category directories"""
        if not self.target_folder.exists():
            print(f"❌ Target folder '{self.target_folder}' does not exist!")
            return False
        
        # Find all category report files
        report_files = list(self.target_folder.glob("*_report.md"))
        
        # Find all category directories (exclude common system/git directories)
        exclude_dirs = {'.git', '__pycache__', '.vscode', '.idea', 'node_modules', '.env'}
        category_dirs = [d for d in self.target_folder.iterdir() 
                        if d.is_dir() and d.name not in exclude_dirs]
        
        print(f"📁 Found {len(report_files)} report files")
        if report_files:
            for rf in report_files:
                print(f"   📄 {rf.name}")
        
        print(f"📁 Found {len(category_dirs)} category directories")
        if category_dirs:
            for cd in category_dirs[:10]:  # Show first 10 
                print(f"   📁 {cd.name}")
            if len(category_dirs) > 10:
                print(f"   ... and {len(category_dirs) - 10} more directories")
        
        # Match reports with directories
        for report_file in report_files:
            # Extract category name from filename (remove _report.md)
            category_name = report_file.stem.replace('_report', '')
            category_dir = self.target_folder / category_name
            
            if category_dir.exists() and category_dir.is_dir():
                # Count files in category
                yaml_files = list(category_dir.glob("*.yaml")) + list(category_dir.glob("*.yml"))
                
                self.category_info[category_name] = {
                    'report_file': report_file,
                    'category_dir': category_dir,
                    'template_count': len(yaml_files),
                    'display_name': category_name.replace('-', ' ').title()
                }
            else:
                print(f"⚠️  No matching directory found for {report_file.name}")
        
        return len(self.category_info) > 0
    
    def move_reports_to_categories(self):
        """Move report files to their corresponding category directories"""
        print("\n🔄 Moving category reports to their directories...")
        
        for category_name, info in self.category_info.items():
            report_file = info['report_file']
            category_dir = info['category_dir']
            target_readme = category_dir / "README.md"
            
            try:
                # Check if README.md already exists
                if target_readme.exists():
                    backup_file = category_dir / "README_backup.md"
                    shutil.move(str(target_readme), str(backup_file))
                    print(f"📄 Backed up existing README in {category_name}")
                
                # Move and rename report file to README.md
                shutil.move(str(report_file), str(target_readme))
                self.moved_reports.append({
                    'category': category_name,
                    'from': str(report_file),
                    'to': str(target_readme),
                    'template_count': info['template_count']
                })
                print(f"✅ Moved {report_file.name} → {category_name}/README.md")
                
            except Exception as e:
                self.failed_moves.append({
                    'category': category_name,
                    'error': str(e)
                })
                print(f"❌ Failed to move {report_file.name}: {e}")
    
    def update_root_readme(self):
        """Update root README to reference category READMEs"""
        root_readme = self.target_folder / "README.md"
        
        if not root_readme.exists():
            print("❌ Root README.md does not exist!")
            return False
        
        print("\n📝 Updating root README.md...")
        
        try:
            # Read current content
            with open(root_readme, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Generate new categories section
            categories_section = self.generate_categories_section()
            
            # Find and replace the Categories Overview section
            pattern = r'## Categories Overview\n.*?(?=\n##|\Z)'
            if re.search(pattern, content, re.DOTALL):
                # Replace existing section
                new_content = re.sub(pattern, categories_section, content, flags=re.DOTALL)
            else:
                # Append to end
                new_content = content + "\n\n" + categories_section
            
            # Write updated content
            with open(root_readme, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ Root README.md updated successfully")
            return True
            
        except Exception as e:
            print(f"❌ Error updating root README: {e}")
            return False
    
    def generate_categories_section(self) -> str:
        """Generate Categories Overview section with links"""
        section = """## Categories Overview

Each category has its own directory with organized templates and detailed documentation.

### 📊 Categories Summary

| Category | Templates | Description |
|----------|-----------|-------------|
"""
        
        # Sort categories by template count (descending)
        sorted_categories = sorted(self.category_info.items(), 
                                 key=lambda x: x[1]['template_count'], 
                                 reverse=True)
        
        for category_name, info in sorted_categories:
            display_name = info['display_name']
            template_count = info['template_count']
            
            # Generate description based on category type
            description = self.get_category_description(category_name)
            
            section += f"| [{display_name}](./{category_name}/README.md) | {template_count} | {description} |\n"
        
        section += f"""
### 📁 Directory Structure

```
./
├── README.md (this file)
"""
        
        for category_name, info in sorted_categories:
            template_count = info['template_count']
            section += f"├── {category_name}/\n"
            section += f"│   ├── README.md ({template_count} templates documented)\n"
            section += f"│   └── *.yaml (nuclei templates)\n"
        
        section += "```\n"
        
        # Add quick navigation
        section += "\n### 🔗 Quick Navigation\n\n"
        
        # Group by type
        tech_categories = []
        attack_categories = []
        other_categories = []
        
        for category_name, info in sorted_categories:
            if category_name.startswith('technology-'):
                tech_categories.append((category_name, info))
            elif category_name.startswith('attack-'):
                attack_categories.append((category_name, info))
            else:
                other_categories.append((category_name, info))
        
        if tech_categories:
            section += "**Technology-based Templates:**\n"
            for category_name, info in tech_categories:
                section += f"- [{info['display_name']}](./{category_name}/README.md) ({info['template_count']} templates)\n"
            section += "\n"
        
        if attack_categories:
            section += "**Attack-based Templates:**\n"
            for category_name, info in attack_categories:
                section += f"- [{info['display_name']}](./{category_name}/README.md) ({info['template_count']} templates)\n"
            section += "\n"
        
        if other_categories:
            section += "**Other Categories:**\n"
            for category_name, info in other_categories:
                section += f"- [{info['display_name']}](./{category_name}/README.md) ({info['template_count']} templates)\n"
        
        return section
    
    def get_category_description(self, category_name: str) -> str:
        """Generate description for category"""
        if category_name.startswith('technology-'):
            tech = category_name.replace('technology-', '')
            return f"Templates targeting {tech.title()} technology"
        elif category_name.startswith('attack-'):
            attack = category_name.replace('attack-', '')
            return f"Templates for {attack.replace('-', ' ').title()} attacks"
        elif category_name == 'cve-vulnerabilities':
            return "CVE-based vulnerability templates"
        elif category_name == 'information-gathering':
            return "Templates for information disclosure and reconnaissance"
        elif category_name == 'configuration-issues':
            return "Templates for detecting configuration problems"
        elif category_name == 'miscellaneous':
            return "Templates that don't fit other categories"
        else:
            return f"Templates in {category_name.replace('-', ' ')} category"
    
    def create_category_index(self):
        """Create index.md file that aggregates all categories"""
        index_file = self.target_folder / "INDEX.md"
        
        print(f"\n📋 Creating category index: {index_file}")
        
        try:
            index_content = f"""# Nuclei Templates Index

This is a comprehensive index of all organized nuclei templates.

## Statistics

- **Total Categories**: {len(self.category_info)}
- **Total Templates**: {sum(info['template_count'] for info in self.category_info.values())}
- **Successfully Organized**: {len(self.moved_reports)} categories

## Categories by Template Count

"""
            
            # Sort by template count
            sorted_categories = sorted(self.category_info.items(), 
                                     key=lambda x: x[1]['template_count'], 
                                     reverse=True)
            
            for i, (category_name, info) in enumerate(sorted_categories, 1):
                index_content += f"{i}. **[{info['display_name']}](./{category_name}/README.md)** - {info['template_count']} templates\n"
            
            # Add categories by type
            index_content += "\n## Categories by Type\n\n"
            
            tech_cats = [c for c in sorted_categories if c[0].startswith('technology-')]
            attack_cats = [c for c in sorted_categories if c[0].startswith('attack-')]
            other_cats = [c for c in sorted_categories if not c[0].startswith(('technology-', 'attack-'))]
            
            if tech_cats:
                index_content += f"### Technology-based ({len(tech_cats)} categories)\n"
                for category_name, info in tech_cats:
                    index_content += f"- [{info['display_name']}](./{category_name}/README.md) ({info['template_count']})\n"
                index_content += "\n"
            
            if attack_cats:
                index_content += f"### Attack-based ({len(attack_cats)} categories)\n"
                for category_name, info in attack_cats:
                    index_content += f"- [{info['display_name']}](./{category_name}/README.md) ({info['template_count']})\n"
                index_content += "\n"
            
            if other_cats:
                index_content += f"### Other Categories ({len(other_cats)} categories)\n"
                for category_name, info in other_cats:
                    index_content += f"- [{info['display_name']}](./{category_name}/README.md) ({info['template_count']})\n"
            
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(index_content)
            
            print(f"✅ Created comprehensive index: {index_file}")
            return True
            
        except Exception as e:
            print(f"❌ Error creating index: {e}")
            return False
    
    def print_summary(self):
        """Print summary of results"""
        print("\n" + "="*60)
        print("🎉 README ORGANIZATION COMPLETED!")
        print("="*60)
        
        print(f"✅ Successfully moved: {len(self.moved_reports)} category reports")
        for report in self.moved_reports:
            print(f"   📄 {report['category']}: {report['template_count']} templates")
        
        if self.failed_moves:
            print(f"\n❌ Failed moves: {len(self.failed_moves)}")
            for failure in self.failed_moves:
                print(f"   🚫 {failure['category']}: {failure['error']}")
        
        print(f"\n📊 Organization Statistics:")
        print(f"   • Total categories: {len(self.category_info)}")
        print(f"   • Total templates: {sum(info['template_count'] for info in self.category_info.values())}")
        print(f"   • Root README updated: ✅")
        print(f"   • Category index created: ✅")
        
        print(f"\n📁 File structure:")
        print(f"   ./")
        print(f"   ├── README.md (updated with category links)")
        print(f"   ├── INDEX.md (comprehensive category index)")
        for category_name in sorted(self.category_info.keys()):
            template_count = self.category_info[category_name]['template_count']
            print(f"   ├── {category_name}/")
            print(f"   │   ├── README.md (detailed documentation)")
            print(f"   │   └── {template_count} × *.yaml files")


def main():
    print("📚 README Organization Tool")
    print("="*40)
    
    organizer = ReadmeOrganizer()
    
    # Scan for reports and categories
    if not organizer.scan_reports_and_categories():
        print("❌ No category reports found to organize!")
        return
    
    print(f"\n📋 Found {len(organizer.category_info)} categories to organize:")
    for category_name, info in organizer.category_info.items():
        print(f"   📁 {category_name}: {info['template_count']} templates")
    
    # Confirm with user
    print("\n" + "="*50)
    print("⚠️  This will:")
    print("   • Move category_report.md files into their directories")
    print("   • Rename them to README.md")
    print("   • Update root README.md with category links")
    print("   • Create comprehensive INDEX.md")
    print("="*50)
    
    choice = input("\nProceed with README organization? [y/N]: ").lower().strip()
    if choice not in ['y', 'yes']:
        print("❌ Organization cancelled by user")
        return
    
    try:
        # Move reports to categories
        organizer.move_reports_to_categories()
        
        # Update root README
        organizer.update_root_readme()
        
        # Create category index
        organizer.create_category_index()
        
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