def filter_prime(arr):
    new_list = []
    for i in arr:
        counter = 0
        for j in range(1, i):
            if i % j == 0:
                counter += 1
        if counter >= 2:
            pass
        else:
            new_list.append(i)

    return new_list


print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))