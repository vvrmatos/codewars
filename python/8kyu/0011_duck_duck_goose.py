#!/usr/bin/env python


from collections import namedtuple
from random import randint
from string import ascii_lowercase

Player = namedtuple("Player", "name")


# solution
def duck_duck_goose(players, goose):
    while goose > len(players):
        goose -= len(players)
    return players[~-goose].name



# simple fixed 'tests'
player_list = [Player(name) for name in ascii_lowercase]

print(duck_duck_goose(player_list, 1))  # expected, a
print(duck_duck_goose(player_list, 3))  # expected, c
print(duck_duck_goose(player_list, 10)) # expected, j
print(duck_duck_goose(player_list, 20)) # expected, t
print(duck_duck_goose(player_list, 30)) # expected, d
print(duck_duck_goose(player_list, 18)) # expected, r
print(duck_duck_goose(player_list, 2))  # expected, b
    

# simple random tests
for i in range(10):
    player_list = [Player(name) for name in ascii_lowercase[randint(0, len(ascii_lowercase) - 1)]]
    goose_number = randint(1, 1000)
    print(duck_duck_goose(player_list, goose_number))
