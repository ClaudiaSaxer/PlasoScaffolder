# -*- coding: utf-8 -*-
"""Helper methods for mapping"""
import os

from jinja2 import Environment
from jinja2 import FileSystemLoader

# Since os.path.abspath() uses the current working directory (cwd)
# os.path.abspath(__file__) will point to a different location if
# cwd has been changed. Hence we preserve the absolute location of __file__.
__file__ = os.path.abspath(__file__)

def _get_template_path(template_path=None) -> str:
  """
  Retrieves the path to the template files

  Args:
    template_path: the path to the templates, if none is given the default
    will be taken

  Returns:the template file path

  """
  if template_path is not None:
    path = os.path.dirname(os.path.abspath(template_path))
    directory_name, base_name = os.path.split(path)
    template_path = os.path.join(directory_name, 'templates')
  return template_path


def _get_template_environment() -> Environment:
  """
  template environment
  :return: the template environment
  """
  return Environment(autoescape=False,
    loader=FileSystemLoader(_get_template_path()), trim_blocks=False)


def render_template(template_filename: str, context: dict) -> str:
  """
  render the template
  :param template_filename: the name of the template
  :param context: the context of the template
  :return: the rendered template
  """
  return _get_template_environment().get_template(template_filename).render(
    context)
