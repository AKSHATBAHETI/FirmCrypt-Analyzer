import os
import csv
from extract_features import extract_features

DATA = []
BASE = "../binaries"

for label, folder in [(1, "crypto"), (0, "non_crypto")]:
    path = os.path.join(BASE, folder)
    for file in os.listdir(path):
        feats = extract_features(os.path.join(path, file))
        feats["label"] = label
        DATA.append(feats)

with open("dataset.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, DATA[0].keys())
    writer.writeheader()
    writer.writerows(DATA)

print("Dataset created")