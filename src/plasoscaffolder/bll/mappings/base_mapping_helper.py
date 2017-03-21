# -*- coding: utf-8 -*-
"""Helper methods for mapping"""
import abc
import jinja2


class BaseMappingHelper(object):
  """Base Mapping Helper base class."""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def _GetTemplateEnvironment(self) -> jinja2.Environment:
    """Returns the template environment.

    Returns:
      jinja2.Environment: jinja2 template environment.
    """

  @abc.abstractmethod
  def RenderTemplate(self, template_filename: str, context: dict) -> str:
    """Renders the template.

    Args:
      template_filename (str): the __name of the template
      context (dict): the context of the template

    Returns:
      str: the rendered template
    """

  @abc.abstractmethod
  def GenerateClassName(self, plugin_name: str) -> str:
    """Generates the class name.

    Args:
      plugin_name (str): the plugin name

    Returns:
      str: the class name
    """
