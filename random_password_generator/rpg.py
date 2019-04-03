#!/usr/bin/env python3
import string
import random
import click
from math import log
from random_password_generator import __version__, __name_desc__


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.argument("pass_length", type=int, metavar="<pass-length>")
@click.option("-n", "number", type=int, help="Number of password to generate.", metavar="<int>")
@click.option("-o", "output", type=click.File("w"), help="Output file.", metavar="<out-file>")
@click.version_option(__version__, "-v", "--version", prog_name=__name_desc__)
def rpg(pass_length: int, number: int, output: click.File) -> None:
    """
    Generate random complex password.
    \f

    :param int pass_length: desire password length
    :param int number: number of password to generate
    :param click.File output: output file
    :return: None
    """
    if pass_length < 12:
        raise click.BadArgumentUsage("<pass-length> MUST BE at least 12 in order to have a strong password")

    if not number:
        number = 1

    if output:
        output.write("Passwords:\n")

    click.echo("Passwords:")
    for n in range(number):
        pw = _generate_random_password(pass_length)
        click.echo(pw)

        if output:
            output.write("{}\n".format(pw))

    entropy = _calculate_entropy(pass_length)
    click.echo("\nThe entropy of generated password is: {}".format(entropy))
    if output:
        output.write("Entropy: {}\n".format(entropy))
    click.echo("""
Password strength is determined with this chart:
< 28 bits\t= Very Weak; might keep out family members
28 - 35 bits\t= Weak; should keep out most people, often good for desktop login passwords
36 - 59 bits\t= Reasonable; fairly secure passwords for network and company passwords
60 - 127 bits\t= Strong; can be good for guarding financial information
128+ bits\t= Very Strong; often overkill""")


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


def _calculate_entropy(pw_len: int) -> float:
    """
    Calculate password entropy

    :param int pw_len: password length
    :return int: calculated entropy
    """
    # E = log_2(R^L), R = pool of unique char, L = password length
    chars_pool = len(string.ascii_lowercase) + len(string.ascii_uppercase) + len(string.digits) + len(
        string.punctuation)
    entropy = log(chars_pool ** pw_len, 2)

    return entropy


# MAIN
if __name__ == "__main__":
    rpg()
