#include <stdio.h>
#include <string.h>
 
void printbinary(unsigned x)
{
    int i;
    for (i = 0; i < 32; i++) {
        putchar(x & 0x80000000 ? '1' : '0');

        if (i % 4 == 3)
            putchar(' ');

        x <<= 1;
    }
    putchar('\n');
}

main()
{
    int p = 20, n = 6;
    int x = 0xABCDEF39;

    printf("x: \t\t\t"); printbinary(x);
    printf("~((~0>>n) << p): \t"); printbinary(~((~0>>n) << p));
}