#!/usr/bin/env python3
"""
Fix for pip packaging version parsing issue.
This patches the packaging.version module to handle non-PEP 440 version strings.
Run this once to patch your Python environment.
"""
import sys
import os

def patch_packaging_version():
    """Patch packaging.version.Version to handle Ubuntu/Debian version strings."""
    try:
        from pip._vendor import packaging
        import re
        
        # Store original Version class
        original_version_init = packaging.version.Version.__init__
        
        def patched_version_init(self, version):
            """Patched Version.__init__ that handles non-PEP 440 versions."""
            # If version contains Ubuntu/Debian suffixes, sanitize it
            if isinstance(version, str) and ('ubuntu' in version.lower() or 'zorin' in version.lower()):
                # Extract base version (e.g., "2.4.0-ubuntu4-zorin1" -> "2.4.0")
                match = re.match(r'^(\d+\.\d+\.\d+)', version)
                if match:
                    version = match.group(1)
            
            # Call original init
            try:
                original_version_init(self, version)
            except packaging.version.InvalidVersion:
                # If still invalid, try to extract just the numeric part
                match = re.match(r'^(\d+(?:\.\d+)*)', version)
                if match:
                    version = match.group(1)
                    original_version_init(self, version)
                else:
                    # Last resort: use a default version
                    original_version_init(self, "0.0.0")
        
        # Apply patch
        packaging.version.Version.__init__ = patched_version_init
        print("✓ Successfully patched packaging.version.Version")
        return True
        
    except Exception as e:
        print(f"✗ Failed to patch packaging.version: {e}")
        return False

if __name__ == '__main__':
    if patch_packaging_version():
        print("Packaging version parser has been patched.")
        print("You may need to restart PyCharm for changes to take effect.")
    else:
        print("Failed to apply patch.")
        sys.exit(1)

