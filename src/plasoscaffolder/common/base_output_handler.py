# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class BaseOutputHandler(metaclass=ABCMeta):
  """Clase representing the Base class for the output handler class"""

  @abstractmethod
  def prompt_info(self, text: str) -> str:
    """A prompt for information

    Args:
      text: the text to prompt

    Returns: the user input
    """
    pass

  @abstractmethod
  def prompt_error(self, text: str) -> str:
    """A prompt for errors

    Args:
      text: the text to prompt

    Returns: the user input
    """
    pass

  @abstractmethod
  def print_info(self, text: str):
    """A echo for infos

    Args:
      text: the text to print
    """
    pass

  @abstractmethod
  def print_error(self, text: str):
    """A echo for errors

    Args:
      text: the text to print
    """
    pass

  @abstractmethod
  def confirm(self, text: str):
    """A confirm, Default Y, if no abort execution

    Args:
      text: The text to confirm
    """
    pass
