#include <windows.h>

void caesar(char *msg, int shift) {
    for (int i = 0; msg[i] != '\0'; i++) {
        msg[i] = msg[i] + shift;
    }
}

int main() {
    char text[] = "SECRET";
    caesar(text, 3);
    return 0;
}

int WINAPI WinMain(HINSTANCE hInst, HINSTANCE hPrev, LPSTR lpCmd, int nShow) {
    return main();
}