# -*- coding: utf-8 -*-
"""Class representing the mapper for the formatter."""
from plasoscaffolder.bll.mappings import base_formatter_mapping
from plasoscaffolder.bll.mappings import base_mapping_helper
from plasoscaffolder.model import formatter_data_model


class FormatterMapper(base_formatter_mapping.BaseFormatterMapper):
  """Class representing the formatter mapper."""

  _FORMATTER_TEMPLATE = 'formatter_template.jinja2'

  def __init__(self, mapping_helper: base_mapping_helper.BaseMappingHelper()):
    """Initializing the init mapper class.

    Args:
      mapping_helper (base_mapping_helper.BaseMappingHelper): the helper class
        for the mapping
    """
    super().__init__()
    self._helper = mapping_helper

  def GetFormatter(self,
                   formatter_data: formatter_data_model.FormatterDataModel
                   ) -> str:
    """Retrieves the formatter.

    Args:
      formatter_data (formatter_data_model.FormatterDataModel): the data for 
          the formatter

    Returns:
      str: the rendered template
    """
    class_name = self._helper.GenerateClassName(formatter_data.PluginName)
    context = {'plugin_name': formatter_data.PluginName,
               'class_name': class_name,
               'queries': formatter_data.Queries}
    rendered = self._helper.RenderTemplate(self._FORMATTER_TEMPLATE, context)
    return rendered
