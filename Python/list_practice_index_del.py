mul3 = list(range(3, 50, 3))
mul5 = list(range(5, 50, 5))

mulA = []
for x in mul5:
    if x in mul3:
        mulA.append(x)
        
mulS = sorted(mul3 + mul5)
del mulS[6]
del mulS[13]
del mulS[20]
