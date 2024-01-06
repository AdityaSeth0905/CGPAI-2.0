# build_exe.py

import subprocess

# Install dependencies from the dependencieslist.txt file
subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

# Use PyInstaller to create a standalone executable
subprocess.run(['pyinstaller', '--onefile', 'CGPAI.py'])

print('Standalone executable created successfully.')
