"""Command line interface."""

import prompt


def welcome_user():
    """Greet player."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name
