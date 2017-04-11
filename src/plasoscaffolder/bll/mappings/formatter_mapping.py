# -*- coding: utf-8 -*-
""" Module representing function for the different files. """
from plasoscaffolder.bll.mappings import base_formatter_mapping
from plasoscaffolder.bll.mappings import base_mapping_helper
from plasoscaffolder.model import formatter_data_model


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

  def GetFormatter(self,
                   formatter_data: formatter_data_model.FormatterDataModel) \
      -> str:
    """Retrieves the formatter.

    Args:
      formatter_data: the data for the formatter

    Returns:
      str: the rendered template
    """
    class_name = self._helper.GenerateClassName(formatter_data.PluginName)
    context = {'plugin_name': formatter_data.PluginName,
               'class_name': class_name,
               'queries': formatter_data.Queries}
    rendered = self._helper.RenderTemplate(self._FORMATTER_TEMPLATE, context)
    return rendered
