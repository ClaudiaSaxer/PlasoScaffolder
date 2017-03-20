# -*- coding: utf-8 -*-
"""fake for parser mapping"""
from plasoscaffolder.bll.mappings.base_mapping_helper import BaseMappingHelper
from plasoscaffolder.bll.mappings.base_parser_mapping import BaseParserMapper


class FakeParserMapper(BaseParserMapper):
  """class representing the fake parser mapper"""

  def __init__(self, template_path: str, mapping_helper: BaseMappingHelper):
    pass

  def get_parser(self, plugin_name: str, events: str) -> str:
    return plugin_name
