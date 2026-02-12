import os
import sys
import pandas as pd
from joblib import load

ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(ROOT)

from analysis.extract_features import extract_features

model = load(os.path.join(os.path.dirname(__file__), "multiclass_model.joblib"))

binary_path = os.path.join(ROOT, "unknown.bin")

features = extract_features(binary_path)
df = pd.DataFrame([features])

pred = model.predict(df)[0]

LABEL_REVERSE = {
    0: "Non-Crypto",
    1: "XOR Weak Crypto",
    2: "Hash-Like",
    3: "Symmetric-Like"
}

print("Prediction:", LABEL_REVERSE[pred])