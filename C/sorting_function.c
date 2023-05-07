#include <stdio.h>
#include <stdlib.h>
#define ARRAYSIZE 10000

int isort(int v[], int n) {
    /* insertion sort */
    int i, j, temp;
    int count = 0;

    for (i = 1; i < n; i++) {
        for (j = i - 1; j >= 0 && v[j] > v[j + 1]; j--) {
            temp = v[j], v[j] = v[j + 1], v[j + 1] = temp;
            count++;
        }
    }
    return count;
}

void copyarray(int a[], int b[], int n) {
    //copy n elements of array b[] to a[] 
    for (int i = 0; i < n; i++) {
        a[i] = b[i];
    }
}

void printarray(int a[], int n) {
    //print n elements of array a[] 
    for (int i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}

main()
{
    int numbers[ARRAYSIZE], data[ARRAYSIZE];
    int i, n, count;

    /* Generate 10,000 random numbers */
    for (i = 0; i < ARRAYSIZE; i++)
        numbers[i] = rand();
    printf("Before sort (the first 8 numbers) : ");
    printarray(numbers, 8);
    printf("\n");

    for (n = 10; n <= ARRAYSIZE; n *= 10) {
        copyarray(data, numbers, n);
        count = isort(data, n);
        printf("After insertion sort (the first 5 numbers) : ");
        printarray(data, 5);
        printf("The number of swaps in insertion sort : %d\n\n", count);
    }
    return 0;
}