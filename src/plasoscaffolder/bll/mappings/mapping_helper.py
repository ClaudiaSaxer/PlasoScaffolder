# -*- coding: utf-8 -*-
"""Helper methods for mapping"""
import os

from jinja2 import Environment
from jinja2 import FileSystemLoader


def _get_template_path():
  """
  the path to the template file
  :param file_name: the name of the file
  :return: the template file path
  """
  path = os.path.dirname(os.path.abspath(__file__))
  head, tail = os.path.split(path)
  return os.path.join(head, 'templates')


def _get_template_environment():
  """
  template environment
  :return: the template environment
  """
  return Environment(autoescape=False,
    loader=FileSystemLoader(_get_template_path()), trim_blocks=False)


def render_template(template_filename, context):
  """
  render the template
  :param template_filename: the name of the template
  :param context: the context of the template
  :return: the rendered template
  """
  return _get_template_environment().get_template(template_filename).render(
    context)
