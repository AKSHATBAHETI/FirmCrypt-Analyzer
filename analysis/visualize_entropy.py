import os
import sys
import pandas as pd
import matplotlib.pyplot as plt


ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(ROOT)

# load dataset
df = pd.read_csv(os.path.join(ROOT, "analysis", "dataset.csv"))

# split by class
crypto = df[df["label"] == 1]["entropy"]
non_crypto = df[df["label"] == 0]["entropy"]

# plot
plt.figure()
plt.hist(crypto, bins=10, alpha=0.7, label="Crypto")
plt.hist(non_crypto, bins=10, alpha=0.7, label="Non-Crypto")
plt.xlabel("Entropy")
plt.ylabel("Frequency")
plt.title("Entropy Distribution: Crypto vs Non-Crypto")
plt.legend()
plt.show()