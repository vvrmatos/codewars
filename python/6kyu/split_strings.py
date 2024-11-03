#!/usr/bin/env python3

import re


def solution(letters):
    if len(letters) % 2:
        letters = letters + "_"
    
    pairs = re.findall(r"\w\w", letters)
    return pairs

