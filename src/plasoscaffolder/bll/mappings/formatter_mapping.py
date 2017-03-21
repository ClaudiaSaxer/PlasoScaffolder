# -*- coding: utf-8 -*-
""" Module representing function for the different files. """
from plasoscaffolder.bll.mappings import base_formatter_mapping
from plasoscaffolder.bll.mappings import base_mapping_helper


class FormatterMapper(base_formatter_mapping.BaseFormatterMapper):
  """Class representing the parser mapper."""

  _FORMATTER_TEMPLATE = 'formatter_template.jinja2'

  def __init__(self, template_path: str,
               mapping_helper: base_mapping_helper.BaseMappingHelper):
    """Initializing the init mapper class.

    Args:
      template_path (str): the path to the template directory
    """
    super().__init__()
    self.__helper = mapping_helper(template_path)

  def GetFormatter(self, plugin_name: str, events: list) -> str:
    """Renders the formatter.

    Args:
      plugin_name (str): the name of the plugin
      events (list): the list of the events

    Returns:
      str: the rendered template
    """
    class_name = self.__helper.GenerateClassName(plugin_name)
    context = {'PluginName': plugin_name, 'class_name': class_name,
               'events': events}
    rendered = self.__helper.RenderTemplate(self._FORMATTER_TEMPLATE, context)
    return rendered
