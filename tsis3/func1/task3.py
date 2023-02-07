"""
4x + 2y = 94
x + y = 35 => x = 35 - y
4(35 - y) + 2y = 94
140 - 4y + 2y = 94
-2y = -46
y = 23
x = 12
"""


def solve(numheads, numlegs):
    chicken = int((4 * numheads - numlegs) / 2)
    rab = int(numheads - chicken)

    return f'Num of chicken is {chicken}. Num of rabbits is {rab}.'


print(solve(35, 94))
