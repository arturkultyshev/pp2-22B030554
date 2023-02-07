def func(arr):
    new_arr = []
    for i in arr:
        if i in new_arr:
            pass
        else:
            new_arr.append(i)
    return new_arr


# print(func([1, 1, 1, 12, 3,  4, 5,  6,  6, 7, 78, 8, 8, 9]))
