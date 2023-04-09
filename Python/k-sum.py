m = int(input("m: "))
n = int(input("n: "))
k = int(input("k: "))

list = []

for i in range(m, n, k):
    list.append(i)

print("리스트:", list)
print("합:", sum(list))
