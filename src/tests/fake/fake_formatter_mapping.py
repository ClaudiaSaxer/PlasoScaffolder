# -*- coding: utf-8 -*-
from plasoscaffolder.bll.mappings.base_formatter_mapping import \
  BaseFormatterMapper
from plasoscaffolder.bll.mappings.base_mapping_helper import BaseMappingHelper


class FakeFormatterMapper(BaseFormatterMapper):
  """class representing the fake parser mapper"""

  def __init__(self, template_path: str, mapping_helper: BaseMappingHelper):
    pass

  def get_formatter(self, plugin_name: str, events: str) -> str:
    return plugin_name


