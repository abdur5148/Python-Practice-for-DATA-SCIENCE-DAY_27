def power(a, b):
    d = {}
    for i in range(a, b+1):
        d[i] = i**2
    return d


var1 = power(1, 3)


print(var1)
