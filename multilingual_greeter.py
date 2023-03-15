def greet(lang, name):
    print(lang + name)


def language_input():
    s = input('1: English\n2: Spanish\n3: French\n')
    if s == '1':
        return 'Hello ', 'What\'s your name? '
    elif s == '2':
        return 'Hola ', '¿Cómo te llamas'
    elif s == '3':
        return 'Bonjour ', 'Comment tu t\'appelles '
    else:
        return 'Howdy', 'What\'s your name partner? '


question = language_input()


def name_input():
    name = input(question[1])
    return name


greet(question[0], name_input())
