from random import randint
import prompt

description = 'Answer "yes" if the number is even, otherwise answer "no".'
questions_to_win = 3


def init(player_name):
    print(description)
    play(player_name)


def generate_number():
    return randint(0, 1000000)


def ask_question(number):
    print('Question: {0}'.format(number))


def get_correct_answer(number):
    return 'yes' if number % 2 == 0 else 'no'


def play(player_name):
    for _ in range(questions_to_win):
        current_number = generate_number()
        ask_question(current_number)
        player_answer = prompt.string('Your answer: ')
        correct_answer = get_correct_answer(current_number)

        if not player_answer == correct_answer:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'."
                  .format(player_answer, correct_answer))
            print("Let's try again, {0}!".format(player_name))
            return

        print('Correct!')

    print('Congratulations, {0}!'.format(player_name))
