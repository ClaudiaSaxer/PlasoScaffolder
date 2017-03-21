# -*- coding: utf-8 -*-
"""output file handler for files"""
from plasoscaffolder.common import base_file_handler
from plasoscaffolder.common import base_output_handler


class OutputHandlerFile(base_output_handler.BaseOutputHandler):
  """Class representing the output handler for a file."""

  def __init__(
      self,
      file_path: str,
      file_handler: base_file_handler.BaseFileHandler()):
    """Initializes File Output Handler.

    Args:
      file_path (str): the path to the file
      fileHandler (BaseFileHandler): the file Handler
    """
    super().__init__()
    self.__file_handler = file_handler
    self.__path = file_path

  def PromptInfo(self, text: str) -> str:
    """A prompt for information with click.
    Use with caution. Endless Loops possible

    Args:
      text (str): the text to  prompt

    Returns:
      str: the user input
    """
    return self.__file_handler.AddContent(self.__path, text)

  def PromptError(self, text: str) -> str:
    """A prompt for errors with click.
    Use with caution. Endless Loops possible

    Args:
      text (str): the text to prompt

    Returns:
      str: the user input
    """
    return self.__file_handler.AddContent(self.__path, text)

  def PrintInfo(self, text: str) -> str:
    """A echo for infos with click.

    Args:
      text (str): the text to print

    Returns: the file the content was added
    """
    return self.__file_handler.AddContent(self.__path, text)

  def PrintError(self, text: str) -> str:
    """A echo for errors with click.

    Args:
      text (str): the text to print

    Returns: the file the content was added
    """
    return self.__file_handler.AddContent(self.__path, text)

  def Confirm(self, text: str):
    """A Confirm, Default Y, if no abort execution.

    Args:
      text (str): The text to Confirm
    """
    raise NotImplementedError
