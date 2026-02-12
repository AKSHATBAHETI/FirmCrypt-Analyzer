import os
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SRC_DIR = os.path.join(BASE_DIR, "data_generation", "crypto")
BIN_DIR = os.path.join(BASE_DIR, "binaries", "hash_like")

os.makedirs(SRC_DIR, exist_ok=True)
os.makedirs(BIN_DIR, exist_ok=True)

C_TEMPLATE = r'''
#include <windows.h>

unsigned int hash(char *s) {{
    unsigned int h = 5381;
    for (int i = 0; s[i]; i++)
        h = ((h << 5) + h) + s[i];
    return h;
}}

int main() {{
    char msg[] = "{msg}";
    hash(msg);
    return 0;
}}

int WINAPI WinMain(HINSTANCE a, HINSTANCE b, LPSTR c, int d) {{
    return main();
}}
'''

messages = ["HELLO", "WORLD", "HASH", "DATA"]

count = 0
for m in messages:
    fname = f"hash_{m}.c"
    c_path = os.path.join(SRC_DIR, fname)
    bin_path = os.path.join(BIN_DIR, fname.replace(".c", ".bin"))

    code = C_TEMPLATE.format(msg=m)

    with open(c_path, "w") as f:
        f.write(code)

    subprocess.run(["gcc", c_path, "-o", bin_path], check=True)
    count += 1

print(f"[+] Generated {count} hash-like binaries")