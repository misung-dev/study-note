def longer(x, y):
    if len(x) > len(y):
        return x
    else:
        return y

print(longer([2, 5, 6], [99, 101]))
print(longer([2, 5, 6] * 2, 4 * [99, 101]))

