# -*- coding: utf-8 -*-
"""Helper methods for mapping"""
from abc import ABCMeta, abstractmethod

from jinja2 import Environment


class BaseMappingHelper(metaclass=ABCMeta):
  @abstractmethod
  def _get_template_environment(self) -> Environment:
    """template environment

    Returns: the Environment
    """
    pass

  @abstractmethod
  def render_template(self, template_filename: str, context: dict) -> str:
    """render the template

    Args:
      template_filename: the name of the template
      context: the context of the template

    Returns: the rendered template
    """
    pass
