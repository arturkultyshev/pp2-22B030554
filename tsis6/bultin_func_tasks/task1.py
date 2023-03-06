def mult(arr):
    res = 1
    for j in arr:
        res *= int(j)
    return res


arr = [1, 2, 3, 4, 5]
for i in arr:
    if not str(i).isdigit():
        raise ValueError('Need only digits')

print(mult(arr))
