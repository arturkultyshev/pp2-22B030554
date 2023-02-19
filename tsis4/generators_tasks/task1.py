def squares(num):
    for i in range(1, num + 1):
        yield i ** 2


number = int(input())
sq = squares(number)

for i in sq:
    print(i)
