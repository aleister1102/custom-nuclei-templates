#!/usr/bin/env python3
"""
Directory Cleanup Script
Xóa các thư mục con sau khi đã phân loại nuclei templates
"""

import os
import sys
import shutil
from pathlib import Path
from typing import List
import time
import argparse

class DirectoryCleanup:
    def __init__(self, exclude_dirs: List[str] = None, delete_all: bool = False):
        self.exclude_dirs = exclude_dirs or [
            '.git', 
            'organized-folder',
            '__pycache__',
            '.vscode',
            '.idea'
        ]
        self.delete_all = delete_all  # Flag to delete all directories (including ones with YAML)
        self.deleted_dirs = []
        self.skipped_dirs = []
        self.errors = []

    def is_directory_empty(self, directory: Path) -> bool:
        """Kiểm tra xem thư mục có rỗng không (chỉ chứa thư mục con rỗng)"""
        try:
            for item in directory.rglob('*'):
                if item.is_file():
                    return False
            return True
        except Exception as e:
            print(f"❌ Error checking directory {directory}: {e}")
            return False

    def get_directory_info(self, directory: Path) -> dict:
        """Lấy thông tin về thư mục"""
        info = {
            'name': directory.name,
            'path': str(directory),
            'size': 0,
            'file_count': 0,
            'dir_count': 0
        }
        
        try:
            for item in directory.rglob('*'):
                if item.is_file():
                    info['file_count'] += 1
                    info['size'] += item.stat().st_size
                elif item.is_dir():
                    info['dir_count'] += 1
        except Exception as e:
            print(f"⚠️  Error getting info for {directory}: {e}")
            
        return info

    def should_delete_directory(self, directory: Path) -> tuple[bool, str]:
        """Xác định xem có nên xóa thư mục này không"""
        # Bỏ qua các thư mục trong exclude list
        if directory.name in self.exclude_dirs:
            return False, f"Excluded directory: {directory.name}"
        
        # Kiểm tra xem thư mục có rỗng không
        if self.is_directory_empty(directory):
            return True, "Empty directory"
        
        # Kiểm tra xem thư mục chỉ chứa các file không phải YAML
        has_yaml = False
        has_other_files = False
        yaml_count = 0
        
        try:
            for item in directory.rglob('*'):
                if item.is_file():
                    if item.suffix.lower() in ['.yaml', '.yml']:
                        has_yaml = True
                        yaml_count += 1
                    else:
                        has_other_files = True
        except Exception:
            return False, "Error scanning directory"
        
        # Nếu delete_all flag được set, xóa tất cả (trừ excluded)
        if self.delete_all:
            if has_yaml:
                return True, f"Contains {yaml_count} YAML templates (FORCED DELETE)"
            elif has_other_files:
                return True, "Contains non-YAML files (FORCED DELETE)"
            else:
                return True, "Empty or no files (FORCED DELETE)"
        
        # Logic cũ: chỉ xóa nếu không có YAML files
        if not has_yaml:
            return True, "No YAML templates found"
        
        # Nếu vẫn có YAML files, không xóa (mode bảo vệ)
        return False, f"Still contains {yaml_count} YAML templates"

    def delete_directory(self, directory: Path) -> bool:
        """Xóa thư mục"""
        try:
            shutil.rmtree(directory)
            return True
        except Exception as e:
            self.errors.append(f"Failed to delete {directory}: {e}")
            return False

    def preview_cleanup(self) -> dict:
        """Xem trước những gì sẽ bị xóa"""
        current_dir = Path('.')
        preview = {
            'to_delete': [],
            'to_keep': [],
            'total_size_freed': 0
        }
        
        print("🔍 Scanning directories for cleanup preview...")
        
        for item in current_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                should_delete, reason = self.should_delete_directory(item)
                dir_info = self.get_directory_info(item)
                dir_info['reason'] = reason
                
                if should_delete:
                    preview['to_delete'].append(dir_info)
                    preview['total_size_freed'] += dir_info['size']
                else:
                    preview['to_keep'].append(dir_info)
        
        return preview

    def cleanup_directories(self, confirm: bool = False) -> dict:
        """Thực hiện cleanup các thư mục"""
        current_dir = Path('.')
        
        print("🧹 Starting directory cleanup...")
        
        for item in current_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                should_delete, reason = self.should_delete_directory(item)
                
                if should_delete:
                    if confirm:
                        if self.delete_directory(item):
                            self.deleted_dirs.append({
                                'name': item.name,
                                'path': str(item),
                                'reason': reason
                            })
                            print(f"✅ Deleted: {item.name} ({reason})")
                        else:
                            print(f"❌ Failed to delete: {item.name}")
                    else:
                        print(f"🗑️  Would delete: {item.name} ({reason})")
                else:
                    self.skipped_dirs.append({
                        'name': item.name,
                        'path': str(item),
                        'reason': reason
                    })
                    print(f"⏭️  Skipped: {item.name} ({reason})")
        
        return {
            'deleted': self.deleted_dirs,
            'skipped': self.skipped_dirs,
            'errors': self.errors
        }

    def format_size(self, size_bytes: int) -> str:
        """Format file size thành human readable"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"

    def print_preview(self, preview: dict):
        """In preview cleanup"""
        print("\n" + "="*60)
        if self.delete_all:
            print("📋 CLEANUP PREVIEW - FORCE MODE")
        else:
            print("📋 CLEANUP PREVIEW - SAFE MODE")
        print("="*60)
        
        print(f"\n🗑️  Directories to DELETE ({len(preview['to_delete'])}):")
        total_files = 0
        yaml_dirs = 0
        for dir_info in preview['to_delete']:
            total_files += dir_info['file_count']
            if "YAML templates" in dir_info['reason']:
                yaml_dirs += 1
                print(f"   📁 {dir_info['name']}: {dir_info['file_count']} files, "
                      f"{self.format_size(dir_info['size'])} - 🚨 {dir_info['reason']}")
            else:
                print(f"   📁 {dir_info['name']}: {dir_info['file_count']} files, "
                      f"{self.format_size(dir_info['size'])} ({dir_info['reason']})")
        
        print(f"\n✅ Directories to KEEP ({len(preview['to_keep'])}):")
        for dir_info in preview['to_keep'][:10]:  # Show first 10
            print(f"   📁 {dir_info['name']}: {dir_info['file_count']} files, "
                  f"{self.format_size(dir_info['size'])} ({dir_info['reason']})")
        if len(preview['to_keep']) > 10:
            print(f"   ... and {len(preview['to_keep']) - 10} more directories")
        
        print(f"\n📊 Summary:")
        print(f"   • Total directories to delete: {len(preview['to_delete'])}")
        if yaml_dirs > 0:
            print(f"   • 🚨 Directories with YAML templates: {yaml_dirs}")
        print(f"   • Total files to remove: {total_files}")
        print(f"   • Disk space to free: {self.format_size(preview['total_size_freed'])}")

    def print_results(self, results: dict):
        """In kết quả cleanup"""
        print("\n" + "="*60)
        print("🎉 CLEANUP COMPLETED!")
        print("="*60)
        
        print(f"✅ Directories deleted: {len(results['deleted'])}")
        for dir_info in results['deleted']:
            print(f"   🗑️  {dir_info['name']} ({dir_info['reason']})")
        
        print(f"\n⏭️  Directories skipped: {len(results['skipped'])}")
        for dir_info in results['skipped'][:5]:  # Show first 5
            print(f"   📁 {dir_info['name']} ({dir_info['reason']})")
        if len(results['skipped']) > 5:
            print(f"   ... and {len(results['skipped']) - 5} more")
        
        if results['errors']:
            print(f"\n❌ Errors: {len(results['errors'])}")
            for error in results['errors']:
                print(f"   🚫 {error}")


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Cleanup nuclei template directories')
    parser.add_argument('--force', '-f', action='store_true', 
                        help='Force delete all directories (including ones with YAML templates)')
    parser.add_argument('--yes', '-y', action='store_true',
                        help='Skip confirmation prompts')
    args = parser.parse_args()
    
    print("🧹 Directory Cleanup Tool")
    print("="*30)
    
    if args.force:
        delete_all = True
        print("⚠️  Force mode enabled via command line - ALL directories will be deleted!")
    else:
        # Ask user about cleanup mode
        print("\n🔍 Cleanup Mode Selection:")
        print("1. 🛡️  Safe mode - Only delete empty directories and directories without YAML templates")
        print("2. 🗑️  Force mode - Delete ALL directories (except protected ones)")
        print("\n⚠️  Force mode will delete directories even if they contain YAML templates!")
        
        while True:
            mode_choice = input("\nSelect mode [1/2]: ").strip()
            if mode_choice == '1':
                delete_all = False
                print("✅ Safe mode selected - Only empty/non-YAML directories will be deleted")
                break
            elif mode_choice == '2':
                delete_all = True
                print("⚠️  Force mode selected - ALL directories will be deleted!")
                break
            else:
                print("Please enter '1' for safe mode or '2' for force mode")
    
    cleanup = DirectoryCleanup(delete_all=delete_all)
    
    # Preview cleanup
    preview = cleanup.preview_cleanup()
    cleanup.print_preview(preview)
    
    if not preview['to_delete']:
        print("\n✨ No directories need to be cleaned up!")
        return
    
    # Confirm with user
    print("\n" + "="*60)
    if delete_all:
        print("🚨 DANGER: FORCE MODE - This will permanently delete ALL directories above!")
        print("🚨 Including directories that still contain YAML templates!")
    else:
        print("⚠️  WARNING: This will permanently delete the directories above!")
    print("Make sure you have already organized your nuclei templates.")
    print("="*60)
    
    # Skip confirmation if --yes flag is used
    if args.yes:
        print("✅ Auto-confirming due to --yes flag")
    else:
        while True:
            if delete_all:
                choice = input("\n🚨 FORCE DELETE - Are you absolutely sure? [yes/NO/preview]: ").lower().strip()
                if choice == 'yes':
                    break
            else:
                choice = input("\nDo you want to proceed? [y/N/preview]: ").lower().strip()
                if choice in ['y', 'yes']:
                    break
            
            if choice in ['n', 'no', '']:
                print("❌ Cleanup cancelled by user")
                return
            elif choice == 'preview':
                cleanup.print_preview(preview)
            else:
                if delete_all:
                    print("Please enter 'yes' to confirm force delete, 'no' to cancel, or 'preview' to see the preview again")
                else:
                    print("Please enter 'y' for yes, 'n' for no, or 'preview' to see the preview again")
    
    # Perform cleanup
    print("\n🧹 Starting cleanup process...")
    time.sleep(2)  # Give user a moment to cancel if needed
    
    results = cleanup.cleanup_directories(confirm=True)
    cleanup.print_results(results)
    
    print(f"\n📄 Cleanup completed! Check 'organized-folder' for your organized templates.")


if __name__ == "__main__":
    main() 