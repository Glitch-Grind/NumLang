#!/usr/bin/env python
"""
Build script for NumLang standalone executable
Run this to create the .exe file
"""

import PyInstaller.__main__
import os
from pathlib import Path

# Get the project directory
project_dir = Path(__file__).parent

# Files to include in the build
data_files = [
    (str(project_dir / "editor.html"), "."),
    (str(project_dir / "fonts"), "fonts"),
]

# Build the executable
PyInstaller.__main__.run([
    str(project_dir / "launcher.py"),
    '--onefile',
    '--windowed',
    '--name=NumLang',
    '--icon=NONE',
    '--add-data=' + ';'.join([f"{src}{os.pathsep}{dest}" for src, dest in data_files]),
    f'--distpath={project_dir / "dist"}',
    f'--buildpath={project_dir / "build"}',
    f'--specpath={project_dir}',
    '--hidden-import=flask',
    '--hidden-import=flask_cors',
])

print("\n" + "=" * 60)
print("Build complete!")
print(f"Executable location: {project_dir / 'dist' / 'NumLang.exe'}")
print("=" * 60)
