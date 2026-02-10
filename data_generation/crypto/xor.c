#include <windows.h>

void xor_encrypt(char *data, char key) {
    for (int i = 0; data[i] != '\0'; i++) {
        data[i] ^= key;
    }
}

int main() {
    char msg[] = "HELLO";
    xor_encrypt(msg, 0xAA);
    return 0;
}

int WINAPI WinMain(HINSTANCE hInst, HINSTANCE hPrev, LPSTR lpCmd, int nShow) {
    return main();
}