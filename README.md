# PCB Fault Detection System

AI-powered PCB defect detection using deep learning.

## Quick Start
``````bash
pip install -r requirements.txt
``````
## 🎯 Quick Demo

**Web Interface:** Open `web_interface.html` in your browser
**API:** `python api\app.py` then visit http://localhost:8000/docs

## 📊 Model Performance

- **Trained on:** 6 defect types
- **Dataset:** [Your dataset size] images
- **mAP@50:** [Run test to get this]
- **Inference time:** 162ms per image

## 🚀 Usage

### 1. Command Line
```bash
python scripts\predict.py your_pcb_image.jpg
```

### 2. Python API
```python
from ultralytics import YOLO
model = YOLO('runs/detect/pcb_defect_detector/weights/best.pt')
results = model.predict('pcb.jpg')
```

### 3. REST API
```bash
python api\app.py
# Visit: http://localhost:8000/docs
```

### 4. Web Interface
Open `web_interface.html` in browser (requires API running)