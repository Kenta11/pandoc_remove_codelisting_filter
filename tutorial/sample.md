---
documentclass: ltjsarticle
title: Sample
author: Kenta Arai
header-includes:
    - \usepackage[margin=1in]{geometry}
    - \usepackage{listings}
    - \lstset{ frame=single }
    - \renewcommand*\lstlistingname{コード}
---
# Source code

[@lst:source_code] shows source code.

```{#lst:source_code .c .numberLines startFrom="1" caption="sample"}
#include <stdio.h>

#define ARRAY_SIZE 100
#define SWAP(type, a, b) {\
    type tmp = a;\
    a = b;\
    b = tmp;\
}

void initSeed(unsigned int seed);
int  makeRand(void);
void makeRandArray(int* array, int array_size);
void bubbleSort(int* array, int array_size);
void printArray(int* array, int array_size);

int
main(const int argc, const char** argv) {
    int array[ARRAY_SIZE];

    // make random array
    initSeed(0xdeadbeef);
    makeRandArray(array, ARRAY_SIZE);
    printArray(array, ARRAY_SIZE);

    // sort array with bubble sorting
    bubbleSort(array, ARRAY_SIZE);
    printArray(array, ARRAY_SIZE);

    return 0;
}

static unsigned int seed_for_makeRand;
void
initSeed(unsigned int seed) {
    seed_for_makeRand = seed;
}

int
makeRand(void) {
    seed_for_makeRand = (seed_for_makeRand >> 1) | (seed_for_makeRand << 31);

    return seed_for_makeRand;
}

void
makeRandArray(int* array, int array_size) {
    while (array_size--)
        array[array_size] = makeRand();
}

void
bubbleSort(int* array, int array_size) {
    for (int j = array_size - 1; j > 0; j--) {
        for (int i = 0; i < j; i++) {
            if (array[i] > array[i+1])
                SWAP(int, array[i], array[i+1]);
        }
    }
}

void
printArray(int* array, int array_size) {
    for (int i = 0; i < array_size; i++) {
        printf("%d\n", array[i]);
    }
    putchar('\n');
}
```
