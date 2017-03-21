# -*- coding: utf-8 -*-
"""base output handler"""
import abc


class BaseOutputHandler(object):
  """Clase representing the Base class for the output handler class"""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def PromptInfo(self, text: str) -> str:
    """A prompt for information.

    Args:
      text (str): the text to prompt

    Returns:
      str: the user input
    """

  @abc.abstractmethod
  def PromptError(self, text: str) -> str:
    """A prompt for errors.

    Args:
      text (str): the text to prompt

    Returns:
      str: the user input
    """

  @abc.abstractmethod
  def PrintInfo(self, text: str):
    """A echo for infos.

    Args:
      text (str): the text to print
    """

  @abc.abstractmethod
  def PrintError(self, text: str):
    """A echo for errors.

    Args:
      text (str): the text to print
    """

  @abc.abstractmethod
  def Confirm(self, text: str):
    """A Confirm, Default Y, if no abort execution.

    Args:
      text (str): The text to Confirm
    """
