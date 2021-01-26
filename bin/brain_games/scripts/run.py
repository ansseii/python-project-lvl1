from bin.brain_games import engine

from bin.brain_games.games import prime, calc, even_numbers, gcd, progression


def run_even_numbers():
    engine.run(even_numbers)


def run_calc():
    engine.run(calc)


def run_gcd():
    engine.run(gcd)


def run_progression():
    engine.run(progression)


def run_prime():
    engine.run(prime)
