from brain_games import engine

from brain_games.games import even_numbers
from brain_games.games import calc
from brain_games.games import gcd
from brain_games.games import progression


def run_even_numbers():
    engine.run(even_numbers)


def run_calc():
    engine.run(calc)


def run_gcd():
    engine.run(gcd)


def run_progression():
    engine.run(progression)
