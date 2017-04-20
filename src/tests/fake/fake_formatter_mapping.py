# -*- coding: utf-8 -*-
"""fake formatter mapper"""
from plasoscaffolder.bll.mappings import base_formatter_mapping
from plasoscaffolder.bll.mappings import base_mapping_helper
from plasoscaffolder.model import formatter_data_model


class FakeFormatterMapper(base_formatter_mapping.BaseFormatterMapper):
  """class representing the fake parser mapper"""

  def __init__(self, mapping_helper: base_mapping_helper.BaseMappingHelper):
    pass

  def GetFormatter(
      self,
      formatter_data: formatter_data_model.FormatterDataModel) -> str:
    return formatter_data.PluginName
