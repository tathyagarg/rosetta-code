#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int int_pow(int x, int y) {
    return (int) (pow(x, y) + 0.5);
}

bool check_condition(int n) {
    return int_pow(n, 2) - int_pow(n - 1, 2) > 1000;
}

int main() {
    int curr = 0;
    while (true) {
        if (check_condition(curr)) {
            printf("The smallest number satisfying this condition is: %d", curr);
            break;
        }
        curr++;
    }
}
