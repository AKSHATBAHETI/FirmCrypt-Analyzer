import os
import sys
import csv

ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(ROOT)

from analysis.extract_features import extract_features

LABEL_MAP = {
    "non_crypto": 0,
    "xor_weak": 1,
    "hash_like": 2,
    "symmetric_like": 3
}

DATA = []

BIN_BASE = os.path.join(ROOT, "binaries")
DATASET_DIR = os.path.join(ROOT, "dataset")
os.makedirs(DATASET_DIR, exist_ok=True)

for class_name, label in LABEL_MAP.items():
    folder = os.path.join(BIN_BASE, class_name)
    if not os.path.exists(folder):
        print(f"[!] Skipping missing folder: {class_name}")
        continue

    for file in os.listdir(folder):
        binary_path = os.path.join(folder, file)
        feats = extract_features(binary_path)
        feats["label"] = label
        DATA.append(feats)

csv_path = os.path.join(DATASET_DIR, "dataset_multiclass.csv")

with open(csv_path, "w", newline="") as f:
    writer = csv.DictWriter(f, DATA[0].keys())
    writer.writeheader()
    writer.writerows(DATA)

print("[+] Multi-class dataset created")