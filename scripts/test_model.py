from ultralytics import YOLO
from pathlib import Path

print('='*60)
print('Testing PCB Defect Detector')
print('='*60)

# Load trained model
model = YOLO('runs/detect/pcb_defect_detector/weights/best.pt')

# Validate model
print('\nRunning validation...')
metrics = model.val()

print('\n' + '='*60)
print('MODEL PERFORMANCE')
print('='*60)
print(f'mAP@50:     {metrics.box.map50:.4f}')
print(f'mAP@50-95:  {metrics.box.map:.4f}')
print(f'Precision:  {metrics.box.mp:.4f}')
print(f'Recall:     {metrics.box.mr:.4f}')
print('='*60)

# Test on sample images
test_dir = Path('data/processed/test/images')
if test_dir.exists():
    test_images = list(test_dir.glob('*.jpg'))[:5]
    
    print(f'\nTesting on {len(test_images)} sample images...')
    
    for img in test_images:
        results = model.predict(img, save=True, project='runs/detect', name='predictions')
        print(f'  ✓ {img.name}')
    
    print(f'\nPredictions saved to: runs/detect/predictions/')

print('\nDone!')