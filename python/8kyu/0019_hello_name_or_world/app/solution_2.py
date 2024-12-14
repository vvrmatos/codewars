#!/usr/bin/env python3

def hello(*name) -> str:
	return f"Hello, {name[0].title()}!" if any(name) else "Hello, World!"
