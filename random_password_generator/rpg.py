#!/usr/bin/env python3
import string
import random
import click
import random_password_generator.messages.messages as msg
from math import log
from random_password_generator import __version__, __name_desc__

_password_entropy_table = """
Password strength is determined with this chart:
< 28 bits\t= Very Weak; might keep out family members
28 - 35 bits\t= Weak; should keep out most people, often good for desktop login passwords
36 - 59 bits\t= Reasonable; fairly secure passwords for network and company passwords
60 - 127 bits\t= Strong; can be good for guarding financial information
128+ bits\t= Very Strong; often overkill"""


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.argument("pass_length", type=int, metavar="<pass-length>")
@click.option("-n", "--number", "number", type=int, default=1, help="Number of password to generate.",
              metavar="<pass-number>")
@click.option("-o", "--output", "output", type=click.File("w"), help="Output file.", metavar="<out-file>")
@click.option("-nL", "--no-lower", "lower", is_flag=True, help="Remove lower-case characters.")
@click.option("-nU", "--no-upper", "upper", is_flag=True, help="Remove upper-case characters.")
@click.option("-nD", "--no-digits", "digits", is_flag=True, help="Remove digits characters.")
@click.option("-nP", "--no-punctuation", "punctuation", is_flag=True, help="Remove punctuation characters.")
@click.option("-v", "--verbose", "verbose", is_flag=True, help="Print verbose output.")
@click.version_option(__version__, "-V", "--version", prog_name=__name_desc__)
def rpg(pass_length: int, number: int, output: click.File, lower: bool, upper: bool, digits: bool,
        punctuation: bool, verbose: bool) -> None:
    """
    Generate random complex password.
    \f

    :param int pass_length: desire password length
    :param int number: number of password to generate
    :param click.File output: output file
    :param bool lower: remove lower-case characters
    :param bool upper: remove upper-case characters
    :param bool digits: remove digits characters
    :param bool punctuation: remove punctuation characters
    :param bool verbose: print verbose output
    :return: None
    """
    msg.Prints.verbose("Checking <pass-length> ({}) validity".format(pass_length), verbose)
    if pass_length > 90 or pass_length < 12:
        raise click.BadArgumentUsage(
            msg.Echoes.error("Invalid value for \"<pass-length>\": 123 is not in the valid range of 12 to 90."))

    msg.Prints.verbose("Loading charsets", verbose)

    # Check at least one charsets type has been selected
    chars = _load_available_character(lower, upper, digits, punctuation)

    msg.Prints.verbose("Charsets loaded\nChecking charsets validity", verbose)

    if not chars:
        raise click.BadOptionUsage("--no-lower, --no-upper, --no-digits, --no-punctuation",
                                   msg.Echoes.error("RPG needs at least one charsets type to generate password."))
    else:
        if lower or upper or digits or punctuation:
            msg.Prints.warning("You are going to generate passwords without one or more of default charsets!")
            msg.Prints.warning(
                "RPG cares a lot for your security, it's recommended to avoid this practice if possible!\n")

    if output:
        output.write("Passwords:\n")

    msg.Prints.verbose("Start to generate passwords", verbose)

    msg.Prints.emphasis("Passwords:")

    for n in range(number):
        pw = _generate_random_password(pass_length, chars)
        msg.Prints.info(pw)

        if output:
            output.write("{}\n".format(pw))

    entropy = _calculate_entropy(pass_length, chars)
    msg.Prints.emphasis("\nThe entropy of generated password is: {}".format(entropy))

    if output:
        output.write("Entropy: {}\n".format(entropy))

    msg.Prints.verbose(_password_entropy_table, verbose)


def _generate_random_password(length: int, charsets: list) -> str:
    """
    Generate random password

    :param int length: password length
    :param list charsets: available characters to use
    :return str: random password
    """
    pw = []
    chars = len(charsets)

    # Shuffle chars to change every password generation
    random.shuffle(charsets)

    for i in range(length):
        # Append random char into generated password
        pw.append(random.choice(charsets[i % chars]))

    random.shuffle(pw)
    return "".join(pw)


def _calculate_entropy(pw_len: int, charsets: list) -> float:
    """
    Calculate password entropy

    :param int pw_len: password length
    :param list charsets: available characters to use
    :return int: calculated entropy
    """
    # E = log_2(R^L), R = pool of unique char, L = password length
    chars_pool = 0
    for chars in charsets:
        chars_pool += len(chars)

    entropy = log(chars_pool ** pw_len, 2)

    return entropy


def _load_available_character(l: bool, u: bool, d: bool, p: bool) -> list:
    """
    Return available characters list

    :param bool l: should add lower-case characters
    :param bool u: should add upper-case characters
    :param bool d: should add digits
    :param bool p: should add punctuation
    :return list:
    """
    chars = []

    if not l:
        chars.append(string.ascii_lowercase)

    if not u:
        chars.append(string.ascii_uppercase)

    if not d:
        chars.append(string.digits)

    if not p:
        chars.append(string.punctuation)

    return chars


# MAIN
if __name__ == "__main__":
    rpg()
