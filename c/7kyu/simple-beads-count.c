// https://www.codewars.com/kata/58712dfa5c538b6fc7000569/train/c


// Solution

// unsigned int countRedBeads (int n) {
//    if (n <= 0)
//        return 0;
//    else
//        return (n - 1) * 2;
// }


// Fully fleshed code (so to speak)

#include <stdio.h>

unsigned int countRedBeads(int n) {
    if (n <= 0)
        return 0; // No red beads needed for 0 or negative blue beads
    else
        return (n - 1) * 2; // Each blue bead (except the first one) has 2 red beads
}

int main() {
    // Test cases
    int test_cases[] = {0, 1, 2, 3, 5, 10, 100};
    int num_test_cases = sizeof(test_cases) / sizeof(test_cases[0]);

    printf("Testing countRedBeads function:\n");
    for (int i = 0; i < num_test_cases; ++i) {
        printf("Blue beads: %d, Red beads: %d\n", test_cases[i], countRedBeads(test_cases[i]));
    }

    return 0;
}

