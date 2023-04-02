# https://www.codewars.com/kata/582aafca2d44a4a4560000e7/train/python

def keep_order(ary: list, val: int) -> int:
    ary.append(val)
    ary.sort()
    return ary.index(val)


print(keep_order([1, 2, 3, 4, 7], 5))
