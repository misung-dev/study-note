mymemo = ['delicious apples', 'fine chochlates']

f = open('memo2.txt', 'w')
for item in mymemo:
         f.write(item + '\n')
f.close()
print(len(mymemo), "items are written into file")
