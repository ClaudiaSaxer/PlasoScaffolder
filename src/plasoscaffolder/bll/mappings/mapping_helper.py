# -*- coding: utf-8 -*-
"""Helper methods for mapping."""
import jinja2
from plasoscaffolder.bll.mappings import base_mapping_helper


class MappingHelper(base_mapping_helper.BaseMappingHelper):
  """Mapping Helper class."""

  def __init__(self, template_path: str):
    """Initializing the mapping __helper class.

    Args:
      template_path (str): the __path to the template directory
    """
    super().__init__()
    self.__template_path = template_path

  @property
  def _GetTemplateEnvironment(self) -> jinja2.Environment:
    """Returns the template environment.

    Returns:
      jinja2.Environment: jinja2 template environment.
    """
    return jinja2.Environment(autoescape=False,
                              loader=jinja2.FileSystemLoader(
                                  self.__template_path),
                              trim_blocks=False)

  def RenderTemplate(self, template_filename: str, context: dict) -> str:
    """Renders the template.

       Args:
         template_filename (str): the __name of the template
         context (dict): the context of the template

       Returns:
         str: the rendered template
       """
    return self._GetTemplateEnvironment.get_template(
        template_filename).render(context)

  def GenerateClassName(self, plugin_name: str) -> str:
    """Generates the class __name.

    Args:
      plugin_name (str): the plugin __name

    Returns:
      str: the class __name
    """
    return plugin_name.replace('_', ' ').title().replace(' ', '')
