import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

df = pd.read_csv("../analysis/dataset.csv")

X = df.drop("label", axis=1)
y = df["label"]

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

dump(model, "crypto_detector.joblib")
print("Model trained & saved")