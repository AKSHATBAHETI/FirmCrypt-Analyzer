import os
import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(ROOT)

from analysis.feature_engineering import prepare_features

df = pd.read_csv(os.path.join(ROOT, "dataset", "dataset_multiclass.csv"))

X, y = prepare_features(df)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

dump(model, os.path.join(os.path.dirname(__file__), "multiclass_model.joblib"))

print("[+] Multi-class model trained and saved")