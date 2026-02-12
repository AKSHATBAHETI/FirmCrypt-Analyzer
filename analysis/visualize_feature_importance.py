import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from joblib import load

ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(ROOT)

df = pd.read_csv(os.path.join(ROOT, "dataset", "dataset_multiclass.csv"))
X = df.drop("label", axis=1)

model = load(os.path.join(ROOT, "model", "multiclass_model.joblib"))

importances = model.feature_importances_

plt.figure()
plt.bar(range(20), sorted(importances, reverse=True)[:20])
plt.title("Top 20 Feature Importances")
plt.show()