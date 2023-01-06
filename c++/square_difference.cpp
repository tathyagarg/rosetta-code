#include <iostream>
#include <bits/stdc++.h>

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
            std::cout << "The smallest number satisfying the condition is: " << curr << std::endl;
            break;
        }
        curr++;
    }
}
