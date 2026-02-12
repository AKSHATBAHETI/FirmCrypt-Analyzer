
#include <windows.h>

unsigned int hash(char *s) {
    unsigned int h = 5381;
    for (int i = 0; s[i]; i++)
        h = ((h << 5) + h) + s[i];
    return h;
}

int main() {
    char msg[] = "WORLD";
    hash(msg);
    return 0;
}

int WINAPI WinMain(HINSTANCE a, HINSTANCE b, LPSTR c, int d) {
    return main();
}
