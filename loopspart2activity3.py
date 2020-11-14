def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, n):
        d = a + b
        a = b
        b = d

        print(a+b)


fib(10)
