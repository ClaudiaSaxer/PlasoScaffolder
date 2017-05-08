# -*- coding: utf-8 -*-
"""Class representing the mapper for the formatter init files."""
from plasoscaffolder.bll.mappings import base_mapping_helper
from plasoscaffolder.bll.mappings import base_sqliteplugin_mapping
from plasoscaffolder.model import init_data_model


class FormatterInitMapping(
    base_sqliteplugin_mapping.BaseSQLitePluginMapper):
  """Class representing the formatter init mapper."""

  _FORMATTER_INIT_TEMPLATE = 'formatter_init_template.jinja2'

  def __init__(self, mapping_helper: base_mapping_helper.BaseMappingHelper()):
    """Initializing the init mapper class.

    Args:
      mapping_helper (base_mapping_helper.BaseMappingHelper): the helper class
          for the mapping
    """
    super().__init__()
    self._helper = mapping_helper

  def GetRenderedTemplate(
      self,
      data: init_data_model.InitDataModel) -> str:
    """Retrieves the formatter.

    Args:
      data (init_data_model.InitDataModel): the data for init file

    Returns:
      str: the rendered template
    """
    context = {'plugin_name': data.plugin_name,
               'is_create_template': data.is_create_template}
    rendered = self._helper.RenderTemplate(
        self._FORMATTER_INIT_TEMPLATE, context)
    return rendered
