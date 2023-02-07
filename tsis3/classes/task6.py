def isPrime(num):
    counter = 0
    for i in range(1, num):
        if num % i == 0:
            counter += 1

    if counter >= 2:
        return False
    else:
        return True


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
new_list = list(filter(lambda x: isPrime(x), my_list))
print(new_list)
