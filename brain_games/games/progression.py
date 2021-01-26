import random

game_rules = 'What number is missing in the progression?'


def generate_progression_length():
    return random.randint(5, 10)


def generate_first_number():
    return random.randint(0, 100)


def generate_step():
    return random.randint(1, 10)


def generate_hidden_number_idx(progression_length):
    return random.randint(0, progression_length - 1)


def make_question_answer():
    initial_number = generate_first_number()
    step = generate_step()
    progression_length = generate_progression_length()
    hidden_number_idx = generate_hidden_number_idx(progression_length)
    progression = ''
    correct_answer = None

    for index in range(progression_length):
        if index == hidden_number_idx:
            correct_answer = initial_number + index * step
            progression += ' ..'
            continue
        progression += ' {0}'.format(str(initial_number + index * step))

    return progression, str(correct_answer)
