# https://www.codewars.com/kata/56a4addbfd4a55694100001f/train/python


def validate_hello(unknown):
    greetings = {
        'hello': 'english',
        'ciao': 'italian',
        'salut': 'french',
        'hallo': 'german',
        'hola': 'spanish',
        'ahoj': 'czech republic',
        'czesc': 'polish'
    }
    breakpoint()    
    for salutation in greetings:
        if salutation in unknown.lower():
            return True
    return False
