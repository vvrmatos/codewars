#!/usr/bin/env python3

def hello(name="") -> str:
    return f"Hello, {name.title()}!" if name else "Hello, World!"
