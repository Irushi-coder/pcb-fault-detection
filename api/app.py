from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from ultralytics import YOLO
import cv2
import numpy as np
from pathlib import Path
import shutil

app = FastAPI(title="PCB Defect Detection API", version="1.0.0")

# Load model at startup
model = YOLO('runs/detect/pcb_defect_detector/weights/best.pt')

@app.get("/")
def home():
    return {
        "message": "PCB Defect Detection API",
        "version": "1.0.0",
        "endpoints": {
            "/detect": "POST - Upload PCB image for defect detection",
            "/health": "GET - Check API health"
        }
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": True}

@app.post("/detect")
async def detect_defects(file: UploadFile = File(...)):
    """Detect defects in uploaded PCB image"""
    
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    # Save uploaded file
    temp_dir = Path("temp")
    temp_dir.mkdir(exist_ok=True)
    temp_path = temp_dir / file.filename
    
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        # Run detection
        results = model.predict(temp_path, conf=0.25)  # or 0.6, 0.7 - test which works best
        # Process results
        defects = []
        for result in results:
            boxes = result.boxes
            
            for box in boxes:
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                bbox = box.xyxy[0].tolist()
                
                defects.append({
                    "type": model.names[class_id],
                    "confidence": round(confidence, 3),
                    "bbox": [round(x, 2) for x in bbox]
                })
        
        # Save annotated image
        output_dir = Path("results/annotated")
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / file.filename
        result.save(str(output_path))
        
        return JSONResponse({
            "filename": file.filename,
            "status": "pass" if len(defects) == 0 else "fail",
            "total_defects": len(defects),
            "defects": defects,
            "annotated_image": str(output_path)
        })
    
    finally:
        # Cleanup
        if temp_path.exists():
            temp_path.unlink()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)