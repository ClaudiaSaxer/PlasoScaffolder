# -*- coding: utf-8 -*-
"""Helper methods for mapping"""
from jinja2 import Environment
from jinja2 import FileSystemLoader
from plasoscaffolder.bll.mappings.base_mapping_helper import BaseMappingHelper


class MappingHelper(BaseMappingHelper):
  def __init__(self, template_path: str):
    """Initializing the mapping helper class.

    Args:
      template_path: the path to the template directory
    """
    super(MappingHelper, self).__init__()
    self.template_path = template_path

  def _get_template_environment(self) -> Environment:
    """template environment

    Returns: the Environment
    """
    return Environment(autoescape=False,
      loader=FileSystemLoader(self.template_path), trim_blocks=False)

  def render_template(self, template_filename: str, context: dict) -> str:
    """render the template

    Args:
      template_filename: the name of the template
      context: the context of the template

    Returns: the rendered template
    """
    return self._get_template_environment().get_template(
      template_filename).render(context)
