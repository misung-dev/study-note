n = int(input("정수 n을 입력하시오: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (i * 2 - 1))
    
for i in range(1, 2 * n):
    print(" " * i + "*" * (2 * n - 1 - i))
