import math

def entropy(data):
    freq = [0] * 256
    for b in data:
        freq[b] += 1

    ent = 0
    for f in freq:
        if f > 0:
            p = f / len(data)
            ent -= p * math.log2(p)
    return ent


def byte_histogram(data):
    freq = [0] * 256
    for b in data:
        freq[b] += 1

    total = len(data)
    return [f / total for f in freq]


def extract_features(binary_path):
    with open(binary_path, "rb") as f:
        data = f.read()

    features = {}

    features["entropy"] = entropy(data)
    features["size"] = len(data)
    features["null_bytes"] = data.count(b"\x00")

    hist = byte_histogram(data)
    for i, val in enumerate(hist):
        features[f"byte_{i}"] = val

    return features