def tetrate(n):
    return n**n


res = 0
for i in range(1, 1001):
    product = tetrate(i)
    res += product

print(res)
