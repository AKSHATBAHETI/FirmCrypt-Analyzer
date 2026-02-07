#include <stdint.h>

void xor_encrypt(uint8_t *data, uint8_t key) {
    for (int i = 0; i < 32; i++) {
        data[i] ^= key;
    }
}

int main() {
    uint8_t buf[32] = "this is secret data........";
    xor_encrypt(buf, 0xAA);
    return 0;
}