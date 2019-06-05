#!/usr/bin/env python3
import click
import requests
import hashlib
import string
import math
import random
import secrets
import random_password_generator.messages.messages as msg
from random_password_generator import __version__, __name_desc__

_password_entropy_table = """
Password strength is determined with this chart:
< 28 bits\t= Very Weak; might keep out family members
28 - 35 bits\t= Weak; should keep out most people, often good for desktop login passwords
36 - 59 bits\t= Reasonable; fairly secure passwords for network and company passwords
60 - 127 bits\t= Strong; can be good for guarding financial information
128+ bits\t= Very Strong; often overkill"""

_available_charsets = {"l", "u", "d", "p"}


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.argument("pass_length", type=int, metavar="<pass-length>")
@click.option("-n", "--number", type=int, default=1, metavar="<pass-number>",
              help="Number of password to generate. (Max 50)")
@click.option("-o", "--output", "output", type=click.File("w"), metavar="<out-file>", help="Output file.")
@click.option("--exclude-charsets", metavar="[l,u,d,p]",
              help="Exclude comma-separated charsets: [l]owercase, [u]ppercase, [d]igits, [p]unctuation.")
@click.option("--no-safe", is_flag=True, help="Do not check passwords in Have I Been Pwned db.")
@click.option("-v", "--verbose", "verbose", is_flag=True, help="Print verbose output.")
@click.version_option(__version__, "-V", "--version", prog_name=__name_desc__)
def rpg(pass_length: int, number: int, output: click.File, exclude_charsets: str, no_safe: bool, verbose: bool) -> None:
    """
    Generate random, entropic, complex and safe password.
    \f

    :param int pass_length: desire password length
    :param int number: number of password to generate. Default is 1
    :param click.File output: output file
    :param str exclude_charsets: comma-separated charsets to exclude. Default is None
    :param bool no_safe: do not check password in Have I Been Pwned db. Default is False
    :param bool verbose: print verbose output. Default is False
    :return: None
    """
    # Check pass_length validity
    msg.Prints.verbose("Checking <pass-length> ({}) validity".format(pass_length), verbose)
    if pass_length > 90 or pass_length < 12:
        raise click.BadArgumentUsage(
            msg.Echoes.error("Invalid value for \"<pass-length>\": {} is not in the valid range of 12 to 90.")
            .format(pass_length))

    # Check number validity
    msg.Prints.verbose("Checking <pass-number> ({}) validity".format(number), verbose)
    if number > 50:
        raise click.BadOptionUsage("number", msg.Echoes.error(
            "Invalid value for \"<pass-number>\": the maximum value accepted is 50."))

    # Load charsets and check the validity
    msg.Prints.verbose("Loading charsets", verbose)
    chars = _get_char_list(exclude_charsets)
    msg.Prints.verbose("Charsets loaded\nChecking charsets validity", verbose)

    # Check at least one charsets type has been selected
    if not chars:
        raise click.BadOptionUsage("--exclude-charsets",
                                   msg.Echoes.error("RPG needs at least one charsets type to generate password."))
    else:
        if not len(chars) == 4:
            # User chose to not use any charsets, print warning message
            msg.Prints.warning("You are going to generate passwords without one or more of default charsets!")
            msg.Prints.warning(
                "RPG cares a lot for your security, it's recommended to avoid this practice if possible!\n")

    # Check if --no-safe option is in use, if so, print a warning message
    if no_safe:
        msg.Prints.warning("You are going to generate passwords without checking if they have been already leaked!")
        msg.Prints.warning(
            "RPG cares a lot for your security, it's recommended to avoid this practice if possible!\n")

    msg.Prints.verbose("Start to generate passwords", verbose)

    # Print loading
    pw_list = []
    with click.progressbar(length=number, label="Generating passwords", show_pos=True) as pw_bar:
        for _ in pw_bar:
            pw = _generate_random_password(pass_length, chars, no_safe)
            if pw is not None:
                pw_list.append(pw)
            else:
                raise click.ClickException(msg.Echoes.error(
                    "An error occurred while querying Have I Been Pwned API. Please retry or use --no-safe option"))

    # Print generated passwords
    if output:
        output.write("Passwords:\n")
    else:
        msg.Prints.emphasis("Passwords:")

    for pw in pw_list:
        if output:
            output.write("{}\n".format(pw))
        else:
            msg.Prints.info(pw)

    # Calculate entropy and print it
    entropy = _get_entropy(pass_length, chars)
    if output:
        output.write("\nEntropy: {}".format(entropy))
    else:
        msg.Prints.emphasis("\nThe entropy of generated password is: {}".format(entropy))

    # Print summary table, only if --verbose or --output
    if output:
        output.write("\n{}".format(_password_entropy_table))
    else:
        msg.Prints.verbose(_password_entropy_table, verbose)


def _get_char_list(charsets_to_exclude: str = None) -> list:
    """
    Return available characters list.

    :param str charsets_to_exclude: charsets to exclude
    :return list: available charsets list
    """
    chars = []

    charsets = {}
    if charsets_to_exclude is not None:
        # Get charsets to use
        charsets = _sanitize_excluded_charsets(charsets_to_exclude) ^ _available_charsets

    # If charsets is empty, take all charsets
    if not bool(charsets):
        charsets = _available_charsets

    for cset in charsets:
        if cset == "l":
            chars.append(string.ascii_lowercase)
        elif cset == "u":
            chars.append(string.ascii_uppercase)
        elif cset == "d":
            chars.append(string.digits)
        elif cset == "p":
            chars.append(string.punctuation)

    return chars


def _sanitize_excluded_charsets(charsets_to_sanitize: str) -> set:
    """
    Sanitize input strings and return set of the excluded charsets.

    :param str charsets_to_sanitize: charsets to exclude string to sanitize
    :return set: charsets to exclude
    """
    set_to_sanitize = set(charsets_to_sanitize.lower().split(","))

    return set_to_sanitize & _available_charsets


def _generate_random_password(length: int, charsets: list, no_safe: bool = False):
    """
    Generate random password.

    :param int length: password length
    :param list charsets: available characters to use
    :param bool no_safe: should check password in Have I Been Pwned db
    :return: str random password | None
    """
    pw = []
    chars = len(charsets)

    # Shuffle chars to change every password generation
    random.shuffle(charsets)

    for i in range(length):
        # Append random char into generated password
        pw.append(secrets.choice(charsets[i % chars]))

    random.shuffle(pw)
    pw = "".join(pw)

    # Check if generated password is in a password leak
    if not no_safe:
        leaks = _is_leaked_password(pw)
        if leaks == 1:
            _generate_random_password(length, charsets)
        elif leaks == 9:
            return None

    return pw


def _is_leaked_password(pw: str) -> int:
    """
    Check whether a password has been previously leaked or not in Have I Been Pwned db.

    :param str pw: password to check
    :return int: status code:
        - 0: password is safe
        - 1: password has been already leaked
        - 9: error while connecting to Have I Been Pwned API
    """
    hibp_api = "https://api.pwnedpasswords.com/range/{}"
    headers = {
        "user-agent": "random-password-generator-cli",
        "api-version": "2"
    }

    # Get the password hash
    hashed_pw = hashlib.sha1(pw.encode('utf-8')).hexdigest()
    pw_hash_prefix = hashed_pw[:5]
    pw_hash_suffix = hashed_pw[5:]

    # Query have i been pwned
    try:
        res = requests.get(hibp_api.format(pw_hash_prefix), headers=headers)
    except Exception:
        return 9

    # Check if the password is safe
    for line in res.text.splitlines():
        leaked_pw_hash = line.split(':')[0]
        if leaked_pw_hash == pw_hash_suffix.upper():
            return 1

    return 0


def _get_entropy(pw_len: int, charsets: list) -> float:
    """
    Calculate password entropy.

    :param int pw_len: password length
    :param list charsets: available characters to use
    :return int: calculated entropy
    """
    # E = log_2(R^L), R = pool of unique char, L = password length
    chars_pool = len("".join(charsets))
    entropy = math.log(chars_pool ** pw_len, 2)
    return entropy


# MAIN
if __name__ == "__main__":
    rpg()
