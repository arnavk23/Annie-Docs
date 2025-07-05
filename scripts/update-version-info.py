"""
Update version information throughout the documentation.
"""

import os
import re
import sys
from pathlib import Path

def update_version_in_file(file_path, version):
    """Update version information in a specific file."""
    if not os.path.exists(file_path):
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update version patterns
        patterns = [
            (r'version:\s*["\']([^"\']+)["\']', f'version: "{version}"'),
            (r'Version:\s*([^\s]+)', f'Version: {version}'),
            (r'v\d+\.\d+\.\d+', f'v{version}'),
            (r'annie-(\d+\.\d+\.\d+)', f'annie-{version}'),
        ]
        
        updated = False
        for pattern, replacement in patterns:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                content = new_content
                updated = True
        
        if updated:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated version in {file_path}")
        
        return updated
    
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python update-version-info.py <version>")
        sys.exit(1)
    
    version = sys.argv[1]
    print(f"Updating documentation to version {version}")
    
    # Files to update
    files_to_update = [
        'mkdocs.yml',
        'docs/index.md',
        'README.md',
        'configs/netlify.toml',
        'configs/vercel.json'
    ]
    
    updated_count = 0
    for file_path in files_to_update:
        if update_version_in_file(file_path, version):
            updated_count += 1
    
    print(f"Updated version information in {updated_count} files")

if __name__ == "__main__":
    main()
