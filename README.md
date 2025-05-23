# Detection-and-Classification-of-Abnormal-Heartbeats-using-ECG-Signals
A deep learning pipeline for 5 class classification of irregular heartbeats (SVEB/VEB/F/Q/N) using ECG signals from MIT-BIH arrhythmia dataset using 1D Custom CNN. 

Overview

This project is a web-based ECG arrhythmia classification tool. It enables users to upload ECG data, processes the signals to extract relevant features, and predicts arrhythmia classes using a deep learning model. The app visualizes the ECG segment with the highest prediction confidence and returns both the predicted class and probability.

Features

Upload and preprocess ECG data from CSV files

Automatic R-peak detection and segment extraction

Deep learning-based arrhythmia classification (classes: N, SVEB, VEB, F, Q)

Visualization of the ECG segment with the highest prediction confidence

REST API for integration and automation

File Structure
File	Purpose
test_processing.py	Preprocessing: Loads ECG, detects R-peaks, extracts segments, saves CSV
app.py	Flask web server: Handles uploads, runs model inference, serves results
ECG_Classification_Revised.ipynb	Example of processed ECG segments with labels (for reference)
Setup Instructions
Prerequisites

Python 3.7+

pip

Install Dependencies

bash
pip install flask flask-cors pandas numpy matplotlib tensorflow scipy
Model File

Place your trained Keras model at the path specified in app.py (replace 'path' with your model's actual file path).

Usage
Step 1: Preprocess ECG Data

Place your raw ECG data in a CSV file (column name: ECG).

Run the preprocessing script to extract R-peak-centered segments:

bash
python test_processing.py
This will generate r_peak_segments.csv containing 360-sample segments centered at detected R-peaks.

Step 2: Start the Web Application

bash
python app.py
The app will be available at http://localhost:5000/.

Step 3: Make Predictions

Open the web interface and upload a processed CSV file (e.g., r_peak_segments.csv).

The app will:

Predict the arrhythmia class for each segment

Display the ECG segment with the highest-confidence prediction

Return the predicted class, probability, and the plot as a base64-encoded image

API Endpoints
Endpoint	Method	Description
/	GET	Home page (upload form)
/predict	POST	Upload CSV, returns predictions and visualization
Sample /predict Request

Form-data: file (CSV file with ECG segments)

Sample Response

json
{
  "output": [0, 1, 0, ...],
  "ecg_plot": "<base64-png>",
  "label": "N",
  "probability": 0.97
}
Arrhythmia Classes
Label	Description
N	Normal
SVEB	Supraventricular Ectopic
VEB	Ventricular Ectopic
F	Fusion Beat
Q	Unknown/Other
Notes
The model expects input segments of length 360 samples, as produced by the preprocessing script.

The output class indices correspond to the classes list in app.py.

For custom datasets, ensure the CSV format matches the expected input.

Example Data
See ECG_Classification_Revised.ipynb for sample ECG segments and labels.

License
MIT License (or specify your license here)

Acknowledgements
Uses SciPy for signal processing

Built with Flask and TensorFlow

