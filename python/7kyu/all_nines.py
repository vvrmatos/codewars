# https://www.codewars.com/kata/664b9dd610985cc3b6784111/train/python


# TODO: FIX PERFORMANCE

from random import randint


def all_nines(x: int):
    """This function goal is to take a non-even number
    and find the first multiplier number that turns that x number
    into a all nines number, e.g all_nines(11) -> 9, because 11 * 9.
    Whereas, all_nines(13) -> 76923, because 13 * 76923 = 999999, and
    no smaller positive integer, when multiplied by 13, generates an integer
    that contains only 9's.
    : x is a number parameter that x <= 4000
    """
    
    if x % 2 == 0:
        return -1
    
    numb = 1
    
    while True:
        result = str(x * numb)
        result = set(result)
        if len(result) == 1 and result.pop() == '9':
            return numb
        
        numb += 1

start = 1
end = 400

for i in range(start, 10 + 1):
    print(all_nines(i), i)
