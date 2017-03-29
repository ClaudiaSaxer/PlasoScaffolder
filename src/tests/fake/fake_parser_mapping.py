# -*- coding: utf-8 -*-
"""fake for parser mapping"""
from plasoscaffolder.bll.mappings import base_mapping_helper
from plasoscaffolder.bll.mappings import base_parser_mapping


class FakeParserMapper(base_parser_mapping.BaseParserMapper):
  """class representing the fake parser mapper"""

  def __init__(self, template_path: str,
               mapping_helper: base_mapping_helper.BaseMappingHelper):
    pass

  def GetParser(self, plugin_name: str, events: [], queries: []) -> str:
    return plugin_name
