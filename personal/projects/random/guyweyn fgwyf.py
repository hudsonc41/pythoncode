import time

start_time = time.time()

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


fibo_100 = fibo(100)
print(fibo(100))

end_time = time.time()

print(f"Time: {end_time - start_time}")
