# ECG Arrhythmia Classification Web App

This project is a web-based ECG arrhythmia classification tool that allows users to upload ECG data, processes the signals to extract features, and predicts arrhythmia classes using a deep learning model. The app visualizes the ECG segment with the highest prediction confidence and returns both the predicted class and its probability.

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
