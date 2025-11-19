from ultralytics import YOLO
import sys

# Load model
model = YOLO('runs/detect/pcb_defect_detector/weights/best.pt')

# Get image path from command line or use test image
if len(sys.argv) > 1:
    image_path = sys.argv[1]
else:
    # Use a test image
    from pathlib import Path
    test_images = list(Path('data/processed/test/images').glob('*.jpg'))
    if test_images:
        image_path = test_images[0]
    else:
        print('No test images found!')
        sys.exit(1)

print(f'Analyzing: {image_path}')

# Make prediction
results = model.predict(
    image_path,
    save=True,
    conf=0.25,  # Confidence threshold
    project='runs/detect',
    name='predictions'
)

# Print results
for result in results:
    boxes = result.boxes
    print(f'\nFound {len(boxes)} defects:')
    
    for box in boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        class_name = model.names[class_id]
        
        print(f'  - {class_name}: {confidence:.2%} confidence')

print(f'\nAnnotated image saved to: runs/detect/predictions/')