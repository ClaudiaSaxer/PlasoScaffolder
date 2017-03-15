# -*- coding: utf-8 -*-

import click
from plasoscaffolder.common.base_output_handler import BaseOutputHandler


class OutputHandlerClick(BaseOutputHandler):
  """Class representing the output handler for click."""

  def __init__(self):
    super().__init__()

  def prompt_info(self, text: str) -> str:
    """A prompt for information with click.

    Args:
      text (str): the text to  prompt

    Returns:
      str: the user input
    """
    click.prompt(text, type=str)

  def prompt_error(self, text: str) -> str:
    """A prompt for errors with click.

    Args:
      text (str): the text to prompt

    Returns:
      str: the user input
    """
    return click.prompt(click.style(text, fg='red'), type=str)

  def print_info(self, text: str):
    """A echo for infos with click.

    Args:
      text (str): the text to print
    """
    click.echo(text)

  def print_error(self, text: str):
    """A echo for errors with click.

    Args:
      text (str): the text to print
    """
    click.echo(text, color='red')

  def confirm(self, text: str):
    """A confirm, Default Y, if no abort execution.

    Args:
      text (str): The text to confirm
    """
    click.confirm(text, abort=True, default=True)
