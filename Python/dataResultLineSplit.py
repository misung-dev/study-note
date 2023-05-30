f = open("data.txt")
line = f.readline()
numbers = line.split()
sum = 0
for x in numbers:
    sum = sum + float(x)

f2 = open('results.txt', 'w')
f2.write("합계: " + str(sum) + '\n')
#print("합계:", sum, file=f2)
f2.close()
