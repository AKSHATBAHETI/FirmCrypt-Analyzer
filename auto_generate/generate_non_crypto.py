import os
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SRC_DIR = os.path.join(BASE_DIR, "data_generation", "non_crypto")
BIN_DIR = os.path.join(BASE_DIR, "binaries", "non_crypto")

os.makedirs(SRC_DIR, exist_ok=True)
os.makedirs(BIN_DIR, exist_ok=True)

C_TEMPLATE = r'''
#include <windows.h>

int compute(int n) {{
    int s = 0;
    for (int i = 0; i < n; i++)
        s += i * {factor};
    return s;
}}

int main() {{
    compute({size});
    return 0;
}}

int WINAPI WinMain(HINSTANCE a, HINSTANCE b, LPSTR c, int d) {{
    return main();
}}
'''

factors = [1,2,3,4]
sizes = [100,200,300,400]

count = 0
for factor in factors:
    for size in sizes:
        fname = f"calc_{factor}_{size}.c"
        c_path = os.path.join(SRC_DIR, fname)
        bin_path = os.path.join(BIN_DIR, fname.replace(".c", ".bin"))

        code = C_TEMPLATE.format(factor=factor, size=size)

        with open(c_path, "w") as f:
            f.write(code)

        subprocess.run(["gcc", c_path, "-o", bin_path], check=True)
        count += 1

print(f"[+] Generated {count} non-crypto binaries")