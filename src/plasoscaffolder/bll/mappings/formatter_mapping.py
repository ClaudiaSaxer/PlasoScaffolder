# -*- coding: utf-8 -*-
""" Module representing function for the different files. """
from plasoscaffolder.bll.mappings import base_formatter_mapping
from plasoscaffolder.bll.mappings import base_mapping_helper


class FormatterMapper(base_formatter_mapping.BaseFormatterMapper):
  """Class representing the parser mapper."""

  _FORMATTER_TEMPLATE = 'formatter_template.jinja2'

  def __init__(self, mapping_helper: base_mapping_helper.BaseMappingHelper()):
    """Initializing the init mapper class.

    Args:
      template_path (str): the path to the template directory
    """
    super().__init__()
    self._helper = mapping_helper

  def GetFormatter(self, plugin_name: str, events: list) -> str:
    """Renders the formatter.

    Args:
      plugin_name (str): the Name of the plugin
      events (list): the list of the events

    Returns:
      str: the rendered template
    """
    class_name = self._helper.GenerateClassName(plugin_name)
    context = {'plugin_name': plugin_name, 'class_name': class_name,
               'events'     : events}
    rendered = self._helper.RenderTemplate(self._FORMATTER_TEMPLATE, context)
    return rendered
