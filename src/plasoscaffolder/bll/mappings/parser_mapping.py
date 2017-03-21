# -*- coding: utf-8 -*-
""" Module representing function for the different files. """
from plasoscaffolder.bll.mappings import base_mapping_helper
from plasoscaffolder.bll.mappings import base_parser_mapping


class ParserMapper(base_parser_mapping.BaseParserMapper):
  """Class representing the parser mapper."""

  _PARSER_TEMPLATE = 'parser_template.jinja2'

  def __init__(self, template_path: str,
               mapping_helper: base_mapping_helper.BaseMappingHelper):
    """Initializing the init mapper class.

    Args:
      template_path (str): the path to the template directory
    """
    super().__init__()
    self.helper = mapping_helper(template_path)

  def GetParser(self, plugin_name: str, events: list) -> str:
    """Renders the parser.

    Args:
      plugin_name (str): the name of the plugin
      events (list): the list of the events

    Returns:
      str: the rendered template
    """
    class_name = self.helper.GenerateClassName(plugin_name)
    context = {'PluginName': plugin_name, 'class_name': class_name,
               'events': events}
    rendered = self.helper.RenderTemplate(self._PARSER_TEMPLATE, context)
    return rendered
