number = []

while True :
    print("Enter numbers. (To finish press 'Enter' key)")
    n = input()
    if len(n) == 0 :
        break
    number.append(float(n))

number.sort()
number_len = len(number)
midIndex = number_len // 2

if number_len % 2 == 0:
    number_median = (number[midIndex - 1] + number[midIndex]) / 2
else :
    number_median = number[midIndex]

print("You entered")
print(number)
print()
print("max :", max(number))
print("min :", min(number))
print(f"median : {number_median:.2f}")
