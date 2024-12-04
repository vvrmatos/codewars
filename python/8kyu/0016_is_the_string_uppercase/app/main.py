import re


def is_uppercase(text):
    return all([x.isupper() if x.isalpha() else True for x in re.findall(r'\w|\s+', text)]) if text else False
