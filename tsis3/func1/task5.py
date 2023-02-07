from itertools import permutations

def permut():
    string = str(input())
    new_list = []
    for i in permutations(string):
        new_list.append(''.join(i))
    print(new_list)

permut()