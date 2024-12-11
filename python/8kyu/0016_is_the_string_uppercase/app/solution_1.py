import re


def is_uppercase(text):
    # convoluted, slow & verbose
    return all([letter.isupper() if letter.isalpha() else True for letter in re.findall(r'\w|\s+', text)]) if text else False if text else True