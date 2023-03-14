def greet(lang, name):
    print(lang + name)


def language_input():
    s = input('1: English\n2: Spanish\n3: French\n')
    if s == '1':
        return 'Hello '
    elif s == '2':
        return 'Hola '
    elif s == '3':
        return 'Bonjour '
    else:
        return 'Howdy'


def name_input():
    name = input('Please provide a name ')
    return name


greet(language_input(), name_input())
