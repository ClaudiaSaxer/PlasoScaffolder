# -*- coding: utf-8 -*-
"""output file handler for files"""

import sys

from plasoscaffolder.common import base_file_handler
from plasoscaffolder.common import base_output_handler


class OutputHandlerFile(base_output_handler.BaseOutputHandler):
  """Class representing the output handler for a file."""

  def __init__(
      self,
      file_path: str,
      file_handler: base_file_handler.BaseFileHandler(),
      prompt_info="",
      prompt_error="",
      confirm=True,
      confirm_amount_same=100):
    """Initializes File Output Handler.

    Args:
      confirm (bool): what the confirmation should be
      file_path (str): the path to the file
      fileHandler (BaseFileHandler): the file Handler
      prompt_error (str): what to return in a prompt error
      prompt_info (str): what to return in a prompt info
      confirm_amount_same (int): how many times to confirm the same amount. 
      Default = 100
    """
    super().__init__()
    self.__prompt_info = prompt_info
    self.__prompt_error = prompt_error
    self.__file_handler = file_handler
    self.__path = file_path
    self.__confirm = confirm
    self.__confirm_counter = 1
    self.__confirm_amount_same = confirm_amount_same

  def PromptInfo(self, text: str) -> str:
    """A prompt for information with click.
    Use with caution. Endless Loops possible

    Args:
      text (str): the text to  prompt

    Returns:
      str: the user input
    """
    self.__file_handler.AddContent(self.__path, text)
    print(text)
    return self.__prompt_info

  def PromptInfoWithDefault(self, text: str, text_type: object,
                            default: object) -> str:
    """A prompt for information, with a default value and a required type.

    Args:
      text (str): the text to prompt
      text_type (object): the type of the input
      default (object): the default value

    Returns:
      str: the user input
    """
    self.__file_handler.AddContent(self.__path, text)
    print(text)
    return self.__prompt_info

  def PromptError(self, text: str) -> str:
    """A prompt for errors.
    Use with caution. Endless Loops possible

    Args:
      text (str): the text to prompt

    Returns:
      str: the user input
    """
    self.__file_handler.AddContent(self.__path, text)
    print(text)
    return self.__prompt_error

  def PrintInfo(self, text: str) -> str:
    """A echo for infos.

    Args:
      text (str): the text to print

    Returns: the file the content was added
    """
    print(text)
    return self.__file_handler.AddContent(self.__path, text)

  def PrintError(self, text: str) -> str:
    """A echo for errors with click.

    Args:
      text (str): the text to print

    Returns: the file the content was added
    """
    print(text)
    return self.__file_handler.AddContent(self.__path, text)

  def Confirm(self, text: str, default=True, abort=True):
    """A confirmation, Default Y, if no abort execution. Use with caution.

     Args:
       text (str): Prompts the user for a confirmation.
       default (bool): the default value.
       abort (bool): if the program should abort

     Returns:
     """
    print(text)

    if self.__confirm_amount_same > self.__confirm_counter:
      self.__confirm_counter += 1
    else:
      self.__confirm = not self.__confirm
      self.__confirm_counter = 0

    if not self.__confirm and abort:
      sys.exit()
    self.__file_handler.AddContent(self.__path, text)
    return self.__confirm