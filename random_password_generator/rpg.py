#!/usr/bin/env python3
import string
import sys
import random
import click
from random_password_generator import __version__, __name_desc__


@click.command()
@click.argument("pass_length", type=int, metavar="<pass-length>")
@click.option("-n", "number", type=int, help="Number of password to generate.", metavar="<int>")
@click.version_option(__version__, prog_name=__name_desc__)
def rpg(pass_length: int, number: int) -> None:
    """
    Generate random complex password
    \f

    :param int pass_length: desire password length
    :param int number: number of password to generate
    :return: None
    """
    if pass_length < 12:
        raise click.BadArgumentUsage("<pass-length> MUST BE at least 12 in order to have a strong password")

    if not number:
        number = 1

    for n in range(number):
        click.echo(_generate_random_password(pass_length))


def _generate_random_password(length: int) -> str:
    """
    Generate random password

    :param int length: password length
    :return str: random password
    """
    chars = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    pw = []

    # Shuffle chars to change every password generation
    random.shuffle(chars)

    for i in range(length):
        # Append random char into generated password
        pw.append(random.choice(chars[i % 4]))

    random.shuffle(pw)
    return "".join(pw)


# MAIN
if __name__ == "__main__":
    rpg(sys.argv[1:])
