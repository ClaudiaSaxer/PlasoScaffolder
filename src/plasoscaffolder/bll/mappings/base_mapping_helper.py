# -*- coding: utf-8 -*-
"""Helper methods for mapping"""
from abc import ABCMeta
from abc import abstractmethod
from jinja2 import Environment


class BaseMappingHelper(metaclass=ABCMeta):
  @abstractmethod
  def _get_template_environment(self) -> Environment:
    """Returns the template environment.

    Returns:
      Environment: the Environment
    """

  @abstractmethod
  def render_template(self, template_filename: str, context: dict) -> str:
    """Renders the template.

    Args:
      template_filename (str): the name of the template
      context (dict): the context of the template

    Returns:
      str: the rendered template
    """
