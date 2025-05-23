import numpy as np
import pandas as pd
from scipy.signal import find_peaks
import csv

# === STEP 1: Load ECG data from CSV ===
def load_ecg_from_csv(file_path):
    ecg_signal = pd.read_csv(file_path)['ECG'].values
    return ecg_signal

# === STEP 2: Detect R-peaks ===
def detect_r_peaks(ecg_signal, sampling_rate=360):
    distance = int(0.25 * sampling_rate)  # 250ms min between R-peaks
    peaks, _ = find_peaks(ecg_signal, distance=distance, prominence=0.5)
    return peaks

# === STEP 3: Extract 360-sample segments centered at R-peaks ===
def extract_segments(ecg_signal, r_peaks, segment_length=360):
    half_len = segment_length // 2
    segments = []

    for peak in r_peaks:
        start = peak - half_len
        end = peak + half_len

        if start >= 0 and end <= len(ecg_signal):
            segment = ecg_signal[start:end]
            segments.append(segment)

    return np.array(segments)

# === STEP 4: Save segments with header ===
def save_segments_to_csv(segments, output_file="r_peak_segments.csv"):
    num_cols = segments.shape[1]
    header = [f"sample_{i+1}" for i in range(num_cols)]

    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)          # Write header row
        writer.writerows(segments)       # Write segment data

    print(f"✅ Segments saved to '{output_file}' with {segments.shape[0]} rows and {segments.shape[1]} columns.")

# === STEP 5: Run Everything ===
def main():
    file_path = "sample.csv"  # ⬅️ Replace with your actual file name
    ecg = load_ecg_from_csv(file_path)

    r_peaks = detect_r_peaks(ecg)
    print(f"Detected {len(r_peaks)} R-peaks.")

    segments = extract_segments(ecg, r_peaks)
    print(f"Extracted {segments.shape[0]} segments of {segments.shape[1]} samples each.")

    save_segments_to_csv(segments)

if __name__ == "__main__":
    main()
