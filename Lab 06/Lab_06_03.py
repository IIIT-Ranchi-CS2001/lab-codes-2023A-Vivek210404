import math

def my_max(iterable: list | tuple | set) -> int:
    max: int = -math.inf
    for i in iterable:
        if i > max:
            max = i
    return max


print(my_max({1, 2, 3, 4, 5}))