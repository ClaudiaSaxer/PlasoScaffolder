# -*- coding: utf-8 -*-
"""fake formatter mapper"""
from plasoscaffolder.bll.mappings import base_formatter_mapping
from plasoscaffolder.bll.mappings import base_mapping_helper


class FakeFormatterMapper(base_formatter_mapping.BaseFormatterMapper):
  """class representing the fake parser mapper"""

  def __init__(self, template_path: str,
               mapping_helper: base_mapping_helper.BaseMappingHelper):
    pass

  def GetFormatter(self, plugin_name: str, events: str) -> str:
    return plugin_name
