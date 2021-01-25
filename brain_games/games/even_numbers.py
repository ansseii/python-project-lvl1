from random import randint

game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_number():
    return randint(0, 100)


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def make_question_answer():
    number = generate_number()
    correct_answer = is_even(number)

    return number, correct_answer
