# -*- coding: utf-8 -*-
"""Helper methods for mapping."""
from jinja2 import Environment
from jinja2 import FileSystemLoader
from plasoscaffolder.bll.mappings.base_mapping_helper import BaseMappingHelper


class MappingHelper(BaseMappingHelper):
  """Mapping Helper class."""

  def __init__(self, template_path: str):
    """Initializing the mapping helper class.

    Args:
      template_path (str): the path to the template directory
    """
    super().__init__()
    self.template_path = template_path

  def _get_template_environment(self) -> Environment:
    """Returns the template environment.

    Returns:
      jinja2.Environment: jinja2 template environment.
    """
    return Environment(autoescape=False,
      loader=FileSystemLoader(self.template_path), trim_blocks=False)

  def render_template(self, template_filename: str, context: dict) -> str:
    """Renders the template.

       Args:
         template_filename (str): the name of the template
         context (dict): the context of the template

       Returns:
         str: the rendered template
       """
    return self._get_template_environment().get_template(
      template_filename).render(context)
