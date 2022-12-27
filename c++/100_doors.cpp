#include <iostream>

int main() {
    bool doors[100] = {false};

    for (int i = 1; i < 101; i++) {
        for (int j = 0; j < 100; j++) {
            if (j % i == 0) {doors[j] = !doors[j];}
        }
    }

    for (int i = 0; i < 100; i++) {
        if (doors[i]) {std::cout << i << " ";}
    }
    return 0;
}
