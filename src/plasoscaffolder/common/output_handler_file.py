# -*- coding: utf-8 -*-
from plasoscaffolder.common.base_file_handler import BaseFileHandler
from plasoscaffolder.common.base_output_handler import BaseOutputHandler


class OutputHandlerFile(BaseOutputHandler):
  """Class representing the output handler for a file."""

  def __init__(self, filepath: str, fileHandler: BaseFileHandler):
    """Initializes File Output Handler.

    Args:
      filepath (str): the path to the file
      fileHandler (BaseFileHandler): the file Handler
    """
    super().__init__()
    self.file_handler = fileHandler()
    self.path = filepath

  def prompt_info(self, text: str) -> str:
    """A prompt for information with click.

    Args:
      text (str): the text to  prompt

    Returns:
      str: the user input
    """
    raise NotImplementedError

  def prompt_error(self, text: str) -> str:
    """A prompt for errors with click.

    Args:
      text (str): the text to prompt

    Returns:
      str: the user input
    """
    raise NotImplementedError

  def print_info(self, text: str) -> str:
    """A echo for infos with click.

    Args:
      text (str): the text to print

    Returns: the file the content was added
    """
    return self.file_handler.add_content(self.path, text)

  def print_error(self, text: str)-> str:
    """A echo for errors with click.

    Args:
      text (str): the text to print

    Returns: the file the content was added
    """
    return self.file_handler.add_content(self.path, text)

  def confirm(self, text: str):
    """A confirm, Default Y, if no abort execution.

    Args:
      text (str): The text to confirm
    """
    raise NotImplementedError
