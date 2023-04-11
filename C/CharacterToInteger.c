#include <stdio.h>

int htoi(char s[]) {
  int decimalNum = 0;
  int i = 0;
  int n = 0;

  while (s[i] != '\0') {
    if (s[i] >= '0' && s[i] <= '9') {
      n = s[i] - '0';
    } else if (s[i] >= 'A' && s[i] <= 'F') {
      n = s[i] - 'A' + 10 ;
    } else {
      break;
    }
    
    decimalNum = decimalNum * 16 + n;
    i += 1;
  }

  return decimalNum;
}

main() {
  printf("ABCDEF ==> %d\n", htoi("ABCDEF"));
  printf("123456 ==> %d\n", htoi("123456"));
  printf("0100 ==> %d\n", htoi("0100"));
}
