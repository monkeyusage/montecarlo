#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

int randint() {
    // randomly choose between 0 or 1 => map it to -1 1
    int rand_num = rand() % 2;
    int choice = 0;
    if (rand_num == 1) {
        choice = 1;
    } else {
        choice = -1;
    };
    return choice;
}

double* random_walk(int steps) {
    double SQRT_STEPS = sqrt((double)steps);
    // int random generator
    time_t t;
    srand((unsigned) time(&t));
    // allocate enough size for numbers
    double* numbers = malloc(sizeof(double) * steps);
    numbers[0] = 1;
    for (int i = 1; i < steps; i++) {
        int y = randint();
        numbers[i] = numbers[i-1] + (y / SQRT_STEPS); 
    }
    return numbers;
}

void free_arr(double* ptr) {
    free(ptr);
}