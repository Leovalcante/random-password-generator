import click


class Prints:
    """Prints class PRINTS messages in various format"""
    @staticmethod
    def emphasis(msg: str) -> None:
        """
        Print emphasis messages.

        :param str msg: message to print
        :return: None
        """
        click.echo(click.style(msg, fg="cyan"))

    @staticmethod
    def error(msg: str) -> None:
        """
        Print error messages.

        :param str msg: message to print
        :return: None
        """
        click.echo(click.style(msg, fg="red"))

    @staticmethod
    def info(msg: str) -> None:
        """
        Print standard messages.

        :param str msg: message to print
        :return: None
        """
        click.echo(msg)

    @staticmethod
    def verbose(msg: str, vrb: bool) -> None:
        """
        Print verbose messages if verbose is enabled.

        :param str msg: message to print
        :param bool vrb: verbose value
        :return: None
        """
        if vrb:
            click.echo(click.style(msg, fg="magenta"))

    @staticmethod
    def warning(msg: str) -> None:
        """
        Print warning messages.

        :param str msg: message to print
        :return: None
        """
        click.echo(click.style(msg, fg="bright_yellow", bold=True))


class Echoes:
    """Echoes class RETURNS messages in various format"""
    @staticmethod
    def emphasis(msg: str) -> str:
        """
        Print emphasis messages.

        :param str msg: message to print
        :return str: colored msg
        """
        return click.style(msg, fg="cyan")

    @staticmethod
    def error(msg: str) -> str:
        """
        Print error messages.

        :param str msg: message to print
        :return str: colored message
        """
        return click.style(msg, fg="red")

    @staticmethod
    def info(msg: str) -> str:
        """
        Print standard messages.

        :param str msg: message to print
        :return str: colored message
        """
        return msg

    @staticmethod
    def verbose(msg: str, vrb: bool) -> str:
        """
        Print verbose messages if verbose is enabled.

        :param str msg: message to print
        :param bool vrb: verbose value
        :return str: colored message
        """
        if vrb:
            return click.style(msg, fg="magenta")

        return ""

    @staticmethod
    def warning(msg: str) -> str:
        """
        Print warning messages.

        :param str msg: message to print
        :return: None
        """
        return click.style(msg, fg="bright_yellow", bold=True)
