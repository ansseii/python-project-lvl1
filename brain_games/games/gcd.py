import random

game_rules = 'Find the greatest common divisor of given numbers.'


def generate_number():
    return random.randint(0, 100)


def find_gcd(first, second):
    return find_gcd(second, first % second) if second else first


def make_question_answer():
    first_number = generate_number()
    second_number = generate_number()
    question = '{0} {1}'.format(first_number, second_number)

    return question, str(find_gcd(first_number, second_number))
