def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b,b+a

for f in fib():
    if f>100:
        break
    print(f)