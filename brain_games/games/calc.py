import random
import operator

game_rules = 'What is the result of the expression?'
operators = {'*': operator.mul, '+': operator.add, '-': operator.sub}


def generate_number():
    return random.randint(0, 100)


def generate_operator():
    operator_char = random.choice(list(operators.keys()))

    return operator_char, operators[operator_char]


def calculate(first_arg, second_arg, applied_operator):
    return applied_operator(first_arg, second_arg)


def make_question_answer():
    first_arg = generate_number()
    second_arg = generate_number()
    operator_char, operator_fun = generate_operator()
    correct_answer = calculate(first_arg, second_arg, operator_fun)
    question = '{0} {1} {2}'.format(first_arg, operator_char, second_arg)

    return question, str(correct_answer)
