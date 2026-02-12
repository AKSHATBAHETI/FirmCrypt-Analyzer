import os
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SRC_DIR = os.path.join(BASE_DIR, "data_generation", "crypto")
BIN_DIR = os.path.join(BASE_DIR, "binaries", "xor_weak")

os.makedirs(SRC_DIR, exist_ok=True)
os.makedirs(BIN_DIR, exist_ok=True)

C_TEMPLATE = r'''
#include <windows.h>

void enc(char *s) {{
    for (int i = 0; s[i]; i++)
        s[i] ^= {key};
}}

int main() {{
    char msg[] = "{msg}";
    enc(msg);
    return 0;
}}

int WINAPI WinMain(HINSTANCE a, HINSTANCE b, LPSTR c, int d) {{
    return main();
}}
'''

keys = [0x11, 0x22, 0x33, 0x44]
messages = ["HELLO", "DATA", "SECRET", "TEST"]

count = 0
for k in keys:
    for m in messages:
        fname = f"xor_{k}_{m}.c"
        c_path = os.path.join(SRC_DIR, fname)
        bin_path = os.path.join(BIN_DIR, fname.replace(".c", ".bin"))

        code = C_TEMPLATE.format(key=k, msg=m)

        with open(c_path, "w") as f:
            f.write(code)

        subprocess.run(["gcc", c_path, "-o", bin_path], check=True)
        count += 1

print(f"[+] Generated {count} XOR weak binaries")