
#include <windows.h>

int compute(int n) {
    int s = 0;
    for (int i = 0; i < n; i++)
        s += i * 2;
    return s;
}

int main() {
    compute(300);
    return 0;
}

int WINAPI WinMain(HINSTANCE a, HINSTANCE b, LPSTR c, int d) {
    return main();
}
