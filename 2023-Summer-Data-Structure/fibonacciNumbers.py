# 피보나치 수열
def fibo(fb):
    a=0
    b=1
    while True:
        a, b = b, a+b #변수 값의 교환
        if b > n: break
        fb.append(b)

n = 10000
fb = [0, 1]
fibo(fb)
print(fb)
print
print("# of fibos", len(fb))
