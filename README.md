Traffic Violation Detection using YOLOv10
📌 Overview

This project presents a Traffic Light Violation Detection System that automatically identifies vehicles violating red traffic signals using a deep learning–based object detection approach. The system leverages YOLOv10, a state-of-the-art real-time object detection model, to detect vehicles and traffic lights from video streams and determine violations based on spatial rules.

The primary objective of the project is to demonstrate how computer vision and deep learning can be applied to intelligent traffic monitoring and smart city applications.

🎯 Objectives

Detect vehicles and traffic lights in real time

Identify red-light violations using a virtual stop line

Capture visual evidence of violations

Achieve real-time performance with high accuracy

Reduce dependency on manual traffic enforcement

🛠️ Tech Stack

Programming Language: Python

Deep Learning Model: YOLOv10 (Ultralytics)

Dataset: COCO 2017 (subset: vehicles and traffic lights)

Libraries & Tools:

OpenCV

NumPy

Ultralytics YOLO

Platform: Windows


Project Structure

Traffic-violation-detection/
│
├── main.py / pmain1.py        # Main execution script
├── detection.py              # Vehicle & traffic light detection
├── utils.py                  # Helper functions
├── requirements.txt          # Dependencies
├── runs/                     # Inference outputs (ignored)
├── weights/                  # Model weights (ignored)
├── README.md                 # Project documentation
└── .gitignore

Methodology

Object Detection
YOLOv10 is used to detect vehicles and traffic lights from each video frame.

Traffic Light State Analysis
The detected traffic light is analyzed to determine its current state (red/green).

Virtual Stop Line Creation
An imaginary horizontal stop line is defined in the video frame.

Violation Detection
If a vehicle crosses the stop line while the traffic light is red, it is marked as a violation.

Evidence Capture
The violating vehicle is highlighted with a bounding box and the frame is saved as evidence.


Dataset Description

Dataset: COCO 2017

Used Classes:

Vehicles (car, bus, truck, motorcycle)

Traffic lights

A focused subset of the dataset is used to improve task-specific performance.


Evaluation Metrics

mAP (mAP50–95) – Detection accuracy

F1-Score – Balance between precision and recall

Inference Latency – Real-time performance evaluation

The system demonstrates strong real-time detection capability with reliable accuracy.

How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/Jaisni-19/Traffic-violation-detection.git
cd Traffic-violation-detection

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Detection
python main.py


🧪 Sample Output

Vehicles detected with bounding boxes

Traffic light state identified

Violating vehicle highlighted

Snapshot captured when violation occurs

🚀 Applications

Smart city traffic monitoring

Automated traffic law enforcement

Intelligent transportation systems

Urban surveillance and analytics

🔮 Future Enhancements

Multi-camera support

License plate recognition

Cloud-based violation storage

Live dashboard for traffic authorities

Improved night-time detection


👨‍💻 Author

Jai
B.Tech Computer Science Engineering
GitHub: https://github.com/Jaisni-19👨‍💻 Author
