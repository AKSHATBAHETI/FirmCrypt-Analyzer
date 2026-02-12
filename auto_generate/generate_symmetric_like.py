import os
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SRC_DIR = os.path.join(BASE_DIR, "data_generation", "crypto")
BIN_DIR = os.path.join(BASE_DIR, "binaries", "symmetric_like")

os.makedirs(SRC_DIR, exist_ok=True)
os.makedirs(BIN_DIR, exist_ok=True)

C_TEMPLATE = r'''
#include <windows.h>

unsigned char table[256] = {{
    {table_values}
}};

void transform(char *s) {{
    for (int i = 0; s[i]; i++)
        s[i] = table[(unsigned char)s[i]];
}}

int main() {{
    char msg[] = "{msg}";
    transform(msg);
    return 0;
}}

int WINAPI WinMain(HINSTANCE a, HINSTANCE b, LPSTR c, int d) {{
    return main();
}}
'''

table_values = ",".join(str(i ^ 0xAA) for i in range(256))
messages = ["BLOCK", "CIPHER", "ROUND", "STATE"]

count = 0
for m in messages:
    fname = f"symmetric_{m}.c"
    c_path = os.path.join(SRC_DIR, fname)
    bin_path = os.path.join(BIN_DIR, fname.replace(".c", ".bin"))

    code = C_TEMPLATE.format(table_values=table_values, msg=m)

    with open(c_path, "w") as f:
        f.write(code)

    subprocess.run(["gcc", c_path, "-o", bin_path], check=True)
    count += 1

print(f"[+] Generated {count} symmetric-like binaries")