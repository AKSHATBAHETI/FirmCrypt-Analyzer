import sys
import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# make project root visible
ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(ROOT)

# load dataset
df = pd.read_csv(os.path.join(ROOT, "analysis", "dataset.csv"))

X = df.drop("label", axis=1)
y = df["label"]

# split data (IMPORTANT)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# predictions
y_pred = model.predict(X_test)

# evaluation
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Accuracy:", acc)
print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["NON-CRYPTO", "CRYPTO"]))