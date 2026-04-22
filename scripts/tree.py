import os
from pathlib import Path

# Folders to hide from the AI
IGNORE = {'.git', '__pycache__', 'venv', '.venv', '.vscode', '.idea', 'build', 'dist'}

def generate_tree(path, indent=""):
    for item in sorted(path.iterdir()):
        if item.name in IGNORE or item.name.startswith('.'):
            continue
        
        print(f"{indent}├── {item.name}")
        if item.is_dir():
            generate_tree(item, indent + "│   ")

if __name__ == "__main__":
    print(f"Project: {Path.cwd().name}")
    generate_tree(Path('.'))
