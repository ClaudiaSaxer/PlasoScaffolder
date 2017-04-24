# -*- coding: utf-8 -*-
"""fake formatter mapper"""
from plasoscaffolder.bll.mappings import base_mapping_helper
from plasoscaffolder.bll.mappings import base_sqliteplugin_mapping
from plasoscaffolder.model import formatter_data_model


class FakeFormatterMapper(base_sqliteplugin_mapping.BaseSQLitePluginMapper):
  """class representing the fake parser mapper"""

  def __init__(self, mapping_helper: base_mapping_helper.BaseMappingHelper):
    pass

  def GetRenderedTemplate(
      self,
      formatter_data: formatter_data_model.FormatterDataModel) -> str:
    return formatter_data.PluginName
