
#include <windows.h>

void enc(char *s) {
    for (int i = 0; s[i]; i++)
        s[i] ^= 51;
}

int main() {
    char msg[] = "TEST";
    enc(msg);
    return 0;
}

int WINAPI WinMain(HINSTANCE a, HINSTANCE b, LPSTR c, int d) {
    return main();
}
