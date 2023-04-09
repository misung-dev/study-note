n = int(input("정수 n을 입력하시오: "))
sum = 0
for i in range(2, n+1, 2):
    sum += i
print(n,"이하의 짝수의 합:",sum)
