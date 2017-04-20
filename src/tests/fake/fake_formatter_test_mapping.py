# -*- coding: utf-8 -*-
"""fake formatter mapper"""
from plasoscaffolder.bll.mappings import base_formatter_test_mapping
from plasoscaffolder.bll.mappings import base_mapping_helper
from plasoscaffolder.model import formatter_test_data_model


class FakeFormatterTestMapper(
    base_formatter_test_mapping.BaseFormatterTestMapper):
  """class representing the fake parser mapper"""

  def __init__(self, mapping_helper: base_mapping_helper.BaseMappingHelper):
    pass

  def GetFormatterTest(
      self,
      formatter_test_data: formatter_test_data_model.FormatterTestDataModel
  ) -> str:
    return formatter_test_data.PluginName