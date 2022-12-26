#include <stdio.h>
#include <stdbool.h>

int main() {
    bool doors[100];
    for (int i = 0; i < 100; i++) {
        doors[i] = false;
    }

    for (int i = 1; i < 101; i++) {
        for (int j = 0; j < 100; j++) {
            if (j % i == 0) {
                doors[j] = !doors[j];
            }
        }
    }

    for (int i = 0; i < 100; i++) {
        if (doors[i]) { printf("%d ", i);}
    }
    printf("");
    return 0;
}

