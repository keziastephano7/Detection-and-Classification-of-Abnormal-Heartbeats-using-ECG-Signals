# ECG Arrhythmia Classification Web App

This project is a web-based ECG arrhythmia classification tool that allows users to upload ECG data, processes the signals to extract features, and predicts arrhythmia classes using a deep learning model. The app visualizes the ECG segment with the highest prediction confidence and returns both the predicted class and its probability.

---

## 🔗 Dataset Link
MITBH Arrhythmia Dataset : https://www.kaggle.com/datasets/taejoongyoon/mitbit-arrhythmia-database

---

## 🚀 Features

- Upload and preprocess ECG data from CSV files
- Automatic R-peak detection and segment extraction
- Deep learning-based arrhythmia classification  
  *(Classes: N, SVEB, VEB, F, Q)*
- Visualization of the ECG segment with the highest prediction confidence
- REST API for integration and automation

---

## 📁 File Structure

| File                          | Purpose                                                   |
|-------------------------------|-----------------------------------------------------------|
| `test_processing.py`          | Preprocessing: Loads ECG, detects R-peaks, extracts segments, saves CSV |
| `app.py`                      | Flask web server: Handles uploads, runs model inference, serves results |
| `ECG_Classification_Revised.ipynb` | Example of processed ECG segments with labels (for reference) |

---

## ⚙️ Setup Instructions

### 📦 Prerequisites

- Python 3.7+
- `pip`

### 📥 Install Dependencies

```bash
pip install flask flask-cors pandas numpy matplotlib tensorflow scipy
```

## 📁 Model File
Place your trained Keras model at the path specified in app.py.

Replace 'path' in the code with your actual model file path.

## 🚀 Usage
### 1. Preprocess ECG Data
Place your raw ECG data in a CSV file with a column named ECG.

Run the preprocessing script to extract R-peak-centered segments:
```bash
python test_processing.py
```
This will generate a file named r_peak_segments.csv containing 360-sample segments centered at detected R-peaks.

### 2. Start the Web Application
```bash
python app.py
```
The app will be available at: http://localhost:5000/

### 3. Make Predictions
Open the web interface.

Upload a processed CSV file (e.g., r_peak_segments.csv).

The app will:

- Predict the arrhythmia class for each segment.

- Display the ECG segment with the highest-confidence prediction.

- Return the predicted class, probability, and a base64-encoded image of the segment.
---
## 🔌 API Endpoints
| Endpoint                       | Method Description                                                   |
|-------------------------------|-----------------------------------------------------------|
| `/GET`          | Home page (upload form) |
| `/predict`                      | POST	Upload CSV, returns predictions and visualization |

### 📝 Sample /predict Request
Form-data: file (CSV file with ECG segments)

### 📤 Sample Response
```json
{
  "output": [0, 1, 0, 0, 0],
  "ecg_plot": "<base64-png>",
  "label": "N",
  "probability": 0.97
}
```
---
## 🩺 Arrhythmia Classes
| Label                          | Description                                                   |
|-------------------------------|-----------------------------------------------------------|
| `N`          | Normal |
| `SVEB`                      | Supraventricular Ectopic |
| `VEB`                      | Ventricular Ectopic |
| `F`                      | Fusion Beat |
| `Q`                      | Unknown/Other |

---
### ⚠️ Note
The model expects input segments of length 360 samples, as produced by the preprocessing script.

The output class indices correspond to the class list in app.py.

For custom datasets, ensure the CSV format matches the expected input format.

### Acknowledgements
Uses SciPy for signal processing

Built with Flask and TensorFlow
