#!/usr/bin/env python3

# length, offset, list
# move window of that LENGTH by OFFSET, return a [[], []] list of lists

def window(length: int, offset: int, lst: list) -> list:
    # 2, 1 -> [0, 1, 2, 3, 4] -> [ [0, 1], [1, 2], [2, 3], [3, 4] ]
    # When length 0, the sliding occurs if there's room for it meaning;
    # window(0, 1, []) -> [[]]
    # window(0, 2, [1, 2, 3]) -> [ [], [] ]

    new_list = []
    new_length = length
    lst_len = len(lst) if length else len(lst) + 1

    for i in range(0, lst_len, offset):
        sub_lst = lst[i:new_length]
        if len(sub_lst) == length:
            new_list.append(sub_lst)
            new_length += offset
    return new_list

r = window(3, 1, [0, 1, 2, 3])
print(r)
