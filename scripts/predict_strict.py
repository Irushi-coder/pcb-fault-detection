from ultralytics import YOLO
from pathlib import Path

model = YOLO('runs/detect/pcb_defect_detector/weights/best.pt')

# Test different confidence thresholds
test_images = list(Path('data/processed/test/images').glob('*.jpg'))[:10]

for conf_threshold in [0.3, 0.4, 0.5, 0.6, 0.7]:
    print(f'\n{"="*60}')
    print(f'Testing with confidence threshold: {conf_threshold}')
    print("="*60)
    
    total_detections = 0
    for img in test_images:
        results = model.predict(img, conf=conf_threshold, verbose=False)
        detections = len(results[0].boxes)
        total_detections += detections
        
        if detections > 0:
            print(f'{img.name}: {detections} defects')
    
    print(f'Total detections: {total_detections}')