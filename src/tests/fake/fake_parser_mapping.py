# -*- coding: utf-8 -*-
"""fake for parser mapping"""
from plasoscaffolder.bll.mappings import base_mapping_helper
from plasoscaffolder.bll.mappings import base_sqliteplugin_mapping
from plasoscaffolder.model import parser_data_model


class FakeParserMapper(base_sqliteplugin_mapping.BaseSQLitePluginMapper):
  """class representing the fake parser mapper"""

  def __init__(self, mapping_helper: base_mapping_helper.BaseMappingHelper):
    pass

  def GetRenderedTemplate(self, parser_data: parser_data_model.ParserDataModel) -> str:
    """Retrieves the parser."""
    return parser_data.PluginName
