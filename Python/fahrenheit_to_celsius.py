fahr = 0
while fahr <= 100:
    celsius = (fahr - 32) * 5 / 9
    print(fahr, "F = %.1f" %celsius, "°C")
    fahr += 10
