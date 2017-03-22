# -*- coding: utf-8 -*-
"""the output file handler for click"""
import click
from plasoscaffolder.common import base_output_handler


class OutputHandlerClick(base_output_handler.BaseOutputHandler):
  """Class representing the output handler for click."""

  def __init__(self):
    super().__init__()

  def PromptInfo(self, text: str) -> str:
    """A prompt for information with click.

    Args:
      text (str): the text to  prompt

    Returns:
      str: the user input
    """
    click.prompt(text, type=str)

  def PromptError(self, text: str) -> str:
    """A prompt for errors with click.

    Args:
      text (str): the text to prompt

    Returns:
      str: the user input
    """
    return click.prompt(click.style(text, fg='red'), type=str)

  def PrintInfo(self, text: str):
    """A echo for infos with click.

    Args:
      text (str): the text to print
    """
    click.echo(text)

  def PrintError(self, text: str):
    """A echo for errors with click.

    Args:
      text (str): the text to print
    """
    click.echo(text, color='red')

  def Confirm(self, text: str):
    """A confirmation, Default Y, if no abort execution.

    Args:
      text (str): Prompts the user for a confirmation.
    """
    click.confirm(text, abort=True, default=True)
