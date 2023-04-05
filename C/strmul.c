#include<stdio.h>

void strmul(char a[], char b[], int n) {
    int aIndex, bIndex;

    aIndex = 0;
    bIndex = 0;

    while ((n > 0)) {
        while ((b[bIndex] != '\0')) {
            a[aIndex] = b[bIndex]; 
            aIndex++;
            bIndex++;
        }

        n--;
        bIndex = 0;
    }
}

void strsum(char to[], char from1[], char from2[]) {
    int i, j;
    
    i = 0;

    while ((to[i] = from1[i]) != '\0') {
        ++i;
    }
    
    j = 0;
    
    while ((to[i] = from2[j]) != '\0') {
        i++;
        j++;
    }
}

main() {
    char s[100], t[100], u[100];

    strmul(t, "abc", 2);
    strmul(u, "DE", 3);
    strsum(s, t, u);

    printf("출력: %s\n", s);
}