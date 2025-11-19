from ultralytics import YOLO
from pathlib import Path
import cv2

model = YOLO('runs/detect/pcb_defect_detector/weights/best.pt')

def analyze_pcb(image_path):
    print(f'\nAnalyzing: {Path(image_path).name}')
    print('-' * 50)
    
    results = model.predict(image_path, conf=0.25)
    
    for result in results:
        boxes = result.boxes
        
        if len(boxes) == 0:
            print('✓ No defects detected - PCB looks good!')
        else:
            print(f'⚠ Found {len(boxes)} defect(s):')
            
            for i, box in enumerate(boxes, 1):
                class_name = model.names[int(box.cls[0])]
                confidence = float(box.conf[0])
                print(f'  {i}. {class_name} ({confidence:.1%} confident)')
        
        # Save annotated image
        output_path = f'runs/detect/results/{Path(image_path).name}'
        Path('runs/detect/results').mkdir(parents=True, exist_ok=True)
        result.save(output_path)
        
        print(f'\n📸 Annotated image saved to: {output_path}')

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python scripts/predict_app.py <image_path>')
        print('\nOr test with sample images:')
        
        test_dir = Path('data/processed/test/images')
        samples = list(test_dir.glob('*.jpg'))[:3]
        
        for img in samples:
            analyze_pcb(img)
    else:
        analyze_pcb(sys.argv[1])