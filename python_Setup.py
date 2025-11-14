import os
from pathlib import Path

# Create directories
folders = [
    "src/data", "src/models", "src/training", "src/inference",
    "api/routes", "api/schemas",
    "data/raw", "data/processed", "data/annotations",
    "models/weights", "tests", "docs", "examples", "scripts"
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)
    Path(folder + "/__init__.py").touch()

# Create .gitignore
gitignore = """# Python
__pycache__/
*.pyc
venv/
env/

# Data
data/raw/
data/processed/
models/weights/
results/

# IDE
.vscode/
.idea/
.DS_Store
"""

with open(".gitignore", "w") as f:
    f.write(gitignore)

# Create requirements.txt
requirements = """torch>=2.0.0
torchvision>=0.15.0
ultralytics>=8.0.0
opencv-python>=4.8.0
numpy>=1.24.0
fastapi>=0.104.0
uvicorn>=0.24.0
"""

with open("requirements.txt", "w") as f:
    f.write(requirements)

# Create README.md
readme = """# PCB Fault Detection System

AI-powered PCB defect detection using deep learning.

## Quick Start
``````bash
pip install -r requirements.txt
``````
"""

with open("README.md", "w") as f:
    f.write(readme)

print("✓ Setup complete!")