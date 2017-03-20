# -*- coding: utf-8 -*-
""" Module representing function for the different files. """
from plasoscaffolder.bll.mappings.base_formatter_mapping import \
  BaseFormatterMapper
from plasoscaffolder.bll.mappings.base_mapping_helper import BaseMappingHelper


class FormatterMapper(BaseFormatterMapper):
  """Class representing the parser mapper."""

  _FORMATTER_TEMPLATE = 'formatter_template.jinja2'

  def __init__(self, template_path: str, mapping_helper: BaseMappingHelper):
    """Initializing the init mapper class.

    Args:
      template_path (str): the path to the template directory
    """
    super().__init__()
    self.helper = mapping_helper(template_path)

  def get_formatter(self, plugin_name: str, events: list) -> str:
    """Renders the formatter.

    Args:
      plugin_name (str): the name of the plugin
      events (list): the list of the events

    Returns:
      str: the rendered template
    """
    class_name = self.helper.generate_class_name(plugin_name)
    context = {'plugin_name': plugin_name, 'class_name': class_name,
               'events'     : events}
    rendered = self.helper.render_template(self._FORMATTER_TEMPLATE, context)
    return rendered
