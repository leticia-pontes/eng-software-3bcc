from random import choice
from termo import Termo, Feedback, Result, InvalidAttempt
# pip install --user termcolor
from termcolor import colored

# pip install --user coverage
# pip install unidecode
# coverage run -m unittest
# coverage report
# coverage html


def to_output(result: Result):
    for c, feedback in result.feedback:
        if feedback == Feedback.RIGHT_PLACE:
            print(colored(c, "green"), end=' ')
        elif feedback == Feedback.WRONG_PLACE:
            print(colored(c, "yellow"), end=' ')
        else:
            print('_', end=' ')
    print()


def main():
    with open('palavras.txt') as input_stream:
        words = list(filter(
            lambda it: len(it) == 5,
            map(str.strip, input_stream.readlines())
        ))
    word = choice(words)
    limit = 5
    counter = 0
    termo = Termo(word, words)
    result = Result(win=False, feedback=None)
    print('Tente adivinhar a palavra')
    while not result.win and counter < limit:
        try:
            guess = input(f'Tentativa: ')
            result = termo.test(guess)
            counter += 1
            to_output(result)
        except InvalidAttempt:
            print('Tente de novo')
    if result.win:
        print('Parabéns')
    else:
        print(word)
        print('Game over')


if __name__ == '__main__':
    main()
