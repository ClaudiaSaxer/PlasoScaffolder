# -*- coding: utf-8 -*-
""" Module representing function for the different files. """
from plasoscaffolder.bll.mappings.base_init_mapping import BaseInitMapper
from plasoscaffolder.bll.mappings.base_mapping_helper import BaseMappingHelper


class InitMapper(BaseInitMapper):
  """Class representing the init mapper."""

  _PARSER_TEMPLATE = 'parser_template.jinja2'

  def __init__(self, template_path: str, mapping_helper: BaseMappingHelper):
    """Initializing the init mapper class.

    Args:
      template_path (str): the path to the template directory
    """
    super().__init__()
    self.helper = mapping_helper(template_path)

  def get_parser(self, plugin_name: str) -> str:
    """Renders the parser.

    Args:
      plugin_name (str): the plugin name

    Returns:
      str: the rendered template
    """
    class_name = self.helper.generate_class_name(plugin_name)
    context = {'plugin_name': plugin_name, 'class_name':class_name}
    rendered = self.helper.render_template(self._PARSER_TEMPLATE, context)
    return rendered
