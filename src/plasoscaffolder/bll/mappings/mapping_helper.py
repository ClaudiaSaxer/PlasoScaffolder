# -*- coding: utf-8 -*-
"""Helper methods for mapping"""
import os

from jinja2 import Environment
from jinja2 import FileSystemLoader

# Since os.path.abspath() uses the current working directory (cwd)
# os.path.abspath(__file__) will point to a different location if
# cwd has been changed. Hence we preserve the absolute location of __file__.
__file__ = os.path.abspath(__file__)

def _get_template_path() -> str:
  """
  Retrieves the path to the template files

  Returns:the template file path

  """
  path = os.path.dirname(os.path.abspath(__file__ ))
  directory_name = os.path.dirname(path)
  template_path = os.path.join(directory_name, 'templates')
  return template_path


def _get_template_environment(template_path=_get_template_path()) -> Environment:
  """
  template environment

  Args:
    template_path: the path to the template folder, if none is given the default will be taken

  Returns: the Environment

  """
  return Environment(autoescape=False,
    loader=FileSystemLoader(template_path), trim_blocks=False)


def render_template(template_filename: str, context: dict) -> str:
  """
  render the template
  :param template_filename: the name of the template
  :param context: the context of the template
  :return: the rendered template
  """
  return _get_template_environment().get_template(template_filename).render(
    context)
