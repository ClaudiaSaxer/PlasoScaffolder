# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from click._unicodefun import click


class OutputHandlerClick(BaseOutputHandler):
  """Clase representing the Base class for the output handler class"""

  @abstractmethod
  def prompt_info(self, text: str) -> str:
    """A prompt for information

    Args:
      text: the text to prompt

    Returns: the user input
    """
    click.prompt(text)

  @abstractmethod
  def prompt_error(self, text: str) -> str:
    """A prompt for errors

    Args:
      text: the text to prompt

    Returns: the user input
    """
    return click.prompt(click.style(text, fg='red'))

  @abstractmethod
  def echo_info(self, text: str):
    """A echo for infos

    Args:
      text: the text to print
    """
    pass

  @abstractmethod
  def echo_error(self, text: str):
    """A echo for errors

    Args:
      text: the text to print
    """
    pass
