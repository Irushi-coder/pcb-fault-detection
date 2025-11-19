from ultralytics import YOLO
import torch

def train_pcb_detector():
    print('PCB Defect Detector - Training')
    print('='*60)
    
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f'Using device: {device}')
    
    print('Loading YOLO model...')
    model = YOLO('yolov8n.pt')
    
    print('Starting training...')
    results = model.train(
        data='data/pcb_data.yaml',
        epochs=50,
        imgsz=640,
        batch=8,
        device=device,
        project='runs/detect',
        name='pcb_defect_detector',
        patience=10,
        save=True,
        plots=True
    )
    
    print('Training Complete!')
    print('Results saved to: runs/detect/pcb_defect_detector')

if __name__ == '__main__':
    train_pcb_detector()
