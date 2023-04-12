# while 루프를 이용하여 자연수를 더하는 프로그램
count = 0
sum = 0
limit = 1000
while sum < limit:
    sum = sum + count
    count = count + 1
print("1부터", count, "까지의 합계:", sum)

