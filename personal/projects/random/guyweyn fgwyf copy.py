import time

start_time = time.time()


def fibo(n):
    if n in [0, 1]:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


fibo_100 = fibo(100)
print(fibo_100)

end_time = time.time()

print(f"Time: {end_time - start_time}")
