#include <stdio.h>

main()
{
    int prime[1000];
    prime[0] = prime[1] = 0; 
    
    for (int p = 2; p <= 999; p += 1) {
        prime[p] = 1; 
    }

    for (int p = 2; p <= 31; p += 1) {
      if (prime[p] == 1) {
        int i = 2;

        while (i * p < 1000) {
          prime[i * p] = 0;
          i += 1;
        }
      }
    } 

   int i = 0;

    for (int p = 2; p <= 999; p += 1) {
      if (prime[p] == 1) {
        printf("%3d ", p);
        
        i += 1;

        if (i % 15 == 0) {
          printf("\n");
        }
      }
    }
}
