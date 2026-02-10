import sys
import os
import pandas as pd
from joblib import load

# make project root visible
ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(ROOT)

from analysis.extract_features import extract_features

model = load(os.path.join(os.path.dirname(__file__), "crypto_detector.joblib"))

binary_path = os.path.join(ROOT, "unknown.bin")

features = extract_features(binary_path)
df = pd.DataFrame([features])

pred = model.predict(df)[0]
print("CRYPTO" if pred == 1 else "NON-CRYPTO")