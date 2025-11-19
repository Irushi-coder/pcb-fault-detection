# Data Directory

## Structure

- `raw/` - Raw PCB images (not tracked in git)
- `processed/` - Preprocessed images (not tracked in git)
- `annotations/` - Annotation files
- `splits/` - Train/val/test split information

## Dataset Preparation

1. Place raw images in `raw/` directory
2. Run preprocessing: `python scripts/prepare_dataset.py`
3. Annotations will be generated in `annotations/`

## Data Format

Images should be in JPG or PNG format with minimum resolution of 1024x1024 pixels.
