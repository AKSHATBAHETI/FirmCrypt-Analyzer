import math

def entropy(data):
    freq = [0]*256
    for b in data:
        freq[b] += 1

    ent = 0
    for f in freq:
        if f > 0:
            p = f / len(data)
            ent -= p * math.log2(p)
    return ent

def extract_features(binary_path):
    with open(binary_path, "rb") as f:
        data = f.read()

    return {
        "entropy": entropy(data),
        "size": len(data),
        "null_bytes": data.count(b'\x00')
    }