from bin.brain_games import cli

questions_for_win = 3


def check_answer(guess, correct_answer):
    return guess == correct_answer


def run(game):
    player_name = cli.welcome_user(game.game_rules)

    for _ in range(questions_for_win):
        question, correct_answer = game.make_question_answer()
        guess = cli.get_answer(question)

        if not check_answer(guess, correct_answer):
            cli.show_wrong_answer_message(player_name, guess, correct_answer)
            break
        cli.show_correct_answer_message()
    else:
        cli.show_you_win_message(player_name)
