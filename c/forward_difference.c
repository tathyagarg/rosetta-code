#include <stdio.h>
#include <stdbool.h>

void forward(int items[], size_t n, int times) {
    if (times == 0) {
        return;
    }

    for (int i = 0; i < n; i++) {
        printf("%d", items[i]);
        if (i != n - 1) {
            printf(", ");
        }
    }

    int new_lis[n - 1];

    for (int i = 0; i < n - 1; i++) {
        new_lis[i] = items[i+1] - items[i];
    }

    printf("\n");
    return forward(new_lis, n - 1, times - 1);
}

int main() {
    int vars[] = {90, 47, 58, 29, 22, 32, 55, 5, 55, 73};
    size_t size = sizeof(vars)/sizeof(int);

    forward(vars, size, 10);
    return 0;
}
