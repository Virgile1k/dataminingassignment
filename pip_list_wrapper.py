#!/usr/bin/env python3
"""
Wrapper script to fix pip list command for PyCharm packaging tool.
This handles packages with non-PEP 440 version strings (like python-apt).
"""
import sys
import subprocess
import json
import re

def sanitize_version(version_str):
    """Convert non-PEP 440 version strings to valid format."""
    # Remove Ubuntu/Debian-specific suffixes like -ubuntu4-zorin1
    # Keep only the base version number
    match = re.match(r'^(\d+\.\d+\.\d+)', version_str)
    if match:
        return match.group(1)
    return version_str

def main():
    try:
        # Run pip list with JSON format
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'list', '--format=json'],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode != 0:
            # If JSON format fails, try regular format and parse it
            result = subprocess.run(
                [sys.executable, '-m', 'pip', 'list'],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode != 0:
                print(result.stderr, file=sys.stderr)
                sys.exit(result.returncode)
            
            # Parse the regular format (not implemented here, fallback to error)
            print(result.stdout)
            sys.exit(0)
        
        # Parse JSON output
        try:
            packages = json.loads(result.stdout)
        except json.JSONDecodeError:
            # If JSON parsing fails, output the raw output
            print(result.stdout)
            sys.exit(0)
        
        # Sanitize versions that might cause issues
        sanitized_packages = []
        for pkg in packages:
            try:
                # Try to validate the version by creating a simple check
                version = pkg.get('version', '')
                # If version contains non-standard characters, sanitize it
                if re.search(r'[^0-9a-zA-Z._+-]', version) or 'ubuntu' in version.lower() or 'zorin' in version.lower():
                    pkg['version'] = sanitize_version(version)
                sanitized_packages.append(pkg)
            except Exception:
                # Skip problematic packages
                continue
        
        # Output sanitized JSON
        print(json.dumps(sanitized_packages, indent=2))
        sys.exit(0)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()

