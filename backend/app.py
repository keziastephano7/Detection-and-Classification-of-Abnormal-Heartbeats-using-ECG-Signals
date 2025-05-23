from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Define class labels
classes = ['N', 'SVEB', 'VEB', 'F', 'Q']

app = Flask(__name__)
CORS(app)

# Load the model once at startup
model = load_model(r'path')

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Read and preprocess data
        df = pd.read_csv(file)
        test_x = df.select_dtypes(include=[np.number]).values
        predictions = model.predict(test_x)

        # Identify the index with the highest prediction confidence
        max_confidences = predictions.max(axis=1)
        max_index = np.argmax(max_confidences)
        pred = predictions[max_index]

        # Plot the ECG signal with the highest confidence prediction
        fig, ax = plt.subplots(figsize=(12, 4))
        ax.plot(test_x[max_index])
        ax.set_title(f'Prediction: {classes[np.argmax(pred)]} (Prob: {pred[np.argmax(pred)]:.2f})')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        buf.close()
        plt.close(fig)

        # Final predictions for all signals
        if predictions.shape[1] == 1:
            output = (predictions > 0.5).astype(int).flatten().tolist()
        else:
            output = predictions.argmax(axis=1).tolist()

        return jsonify({
            'output': output,
            'ecg_plot': image_base64,
            'label': classes[np.argmax(pred)],
            'probability': float(pred[np.argmax(pred)])
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
