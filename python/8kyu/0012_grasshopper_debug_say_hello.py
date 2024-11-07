#!/usr/bin/env python


data = ["Mr. Spock", "Captain Kirk", "Liutenant Uhura", "Dr. McCoy", "Mr. Scott"]


# solution
def say_hello(name):
    return f"Hello, {name}"


# test
for name in data:
    print(say_hello(name))

