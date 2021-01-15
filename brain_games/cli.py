"""Command line interface."""

import prompt


def welcome_user():
    """Greet player."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!', name)
