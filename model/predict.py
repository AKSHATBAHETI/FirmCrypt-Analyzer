from joblib import load
from analysis.extract_features import extract_features
import pandas as pd

model = load("crypto_detector.joblib")

features = extract_features("unknown.bin")
df = pd.DataFrame([features])

pred = model.predict(df)[0]
print("CRYPTO" if pred == 1 else "NON-CRYPTO")