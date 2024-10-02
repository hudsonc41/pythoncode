fibo_ns = {}


def fibo(n):
    if n in fibo_ns:
        return fibo_ns[n]
    if n in [0, 1]:
        result = 1
    else:
        result = fibo(n - 1) + fibo(n - 2)
    fibo_ns[n] = result
    return result
