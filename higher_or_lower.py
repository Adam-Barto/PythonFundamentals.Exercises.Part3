import random


def computer_number():
    return random.randrange(10)


comp_guess = computer_number()


def evaluate(comp, player):
    if comp > player:
        return 'Too Low!'
    elif comp < player:
        return 'Too High!'
    else:
        return 'Correct!'


def user():
    return input('Please provide a number between 0 and 10. ')


user_guess = user()


def answer(s):
    if s == 'Too Low!':
        print(s)
    elif s == 'Too High!':
        print(s)
    else:
        print(s)
    print('The random number was ' + str(comp_guess))
    print('Your guess was ' + str(user_guess))


answer(evaluate(int(comp_guess), int(user_guess)))
