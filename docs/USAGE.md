\# PCB Defect Detection System - Usage Guide



\## Quick Start



\### Option 1: Command Line

```bash

python scripts\\predict.py path\\to\\pcb\_image.jpg

```



\### Option 2: API



Start the server:

```bash

python api\\app.py

```



Make a request:

```bash

curl -X POST "http://localhost:8000/detect" -F "file=@pcb\_image.jpg"

```



\### Option 3: Web Interface



1\. Start API: `python api\\app.py`

2\. Open: `web\_interface.html` in browser

3\. Upload PCB image

4\. Click "Analyze PCB"



\## Detected Defect Types



1\. Missing\_hole

2\. Spurious\_copper

3\. Spur

4\. Short

5\. Open\_circuit

6\. Mouse\_bite



\## Performance Metrics



Run validation:

```bash

python scripts\\test\_model.py

```



\## Retraining



To retrain with new data:

1\. Add images to `data/raw/\[defect\_type]/`

2\. Run: `python scripts\\prepare\_pcb\_dataset.py`

3\. Run: `python scripts\\train\_model.py`



\## Deployment



\### Docker

```bash

docker build -t pcb-detection .

docker run -p 8000:8000 pcb-detection

```



\### Cloud (AWS/Azure/GCP)

Deploy the API using the Dockerfile provided.

