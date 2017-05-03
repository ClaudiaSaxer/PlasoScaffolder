# -*- coding: utf-8 -*-
"""To Format the code """
import os

from plasoscaffolder.common import base_code_formatter
from yapf.yapflib import yapf_api


class CodeFormatter(base_code_formatter.BaseCodeFormatter):
  """Class handles the code formation of files."""

  def __init__(self):
    """Initializing the code formatter."""
    super().__init__()

  def Format(self, code: str) -> str:
    """Formats the code.
    
    Args:
      code (str): the code to format

    Returns:
      str: the formatted code.
    """
    return yapf_api.FormatCode(code,style_config='.style.yapf')

