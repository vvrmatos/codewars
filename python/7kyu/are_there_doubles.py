def double_check(letters):
    letters = letters.lower()
    return any(True for i, _ in enumerate(letters[:-1]) if letters[i] == letters[i + 1])
