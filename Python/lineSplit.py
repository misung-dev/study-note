line = input('숫자입력: ')
numbers = line.split()
sum = 0
for x in numbers:
    sum = sum + float(x)
print("합계:", sum)
