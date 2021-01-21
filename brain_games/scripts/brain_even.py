#!/usr/bin/env python3
"""Even numbers game."""
from brain_games import cli
from brain_games.games.even_numbers_game_logic import init


def main():
    """Run game."""
    print('Welcome to the Brain Games!')
    player_name = cli.welcome_user()
    init(player_name)


if __name__ == '__main__':
    main()
