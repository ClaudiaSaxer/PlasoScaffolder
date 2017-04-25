# -*- coding: utf-8 -*-
"""Class representing the mapper for the parser file."""
from plasoscaffolder.bll.mappings import base_mapping_helper
from plasoscaffolder.bll.mappings import base_parser_mapping
from plasoscaffolder.model import parser_data_model


class ParserMapper(base_parser_mapping.BaseParserMapper):
  """Class representing the parser mapper."""

  _PARSER_TEMPLATE = 'parser_template.jinja2'

  def __init__(self, mapping_helper: base_mapping_helper.BaseMappingHelper()):
    """Initializing the init mapper class.

    Args:
      mapping_helper (base_mapping_helper.BaseMappingHelper): the helper class
          for the mapping
    """
    super().__init__()
    self.__helper = mapping_helper

  def GetParser(self, parser_data: parser_data_model.ParserDataModel) -> str:
    """Retrieves the parser.

    Args:
      parser_data (parser_data_model.ParserDataModel): the data for the parser

    Returns:
      str: the rendered template
    """
    class_name = self.__helper.GenerateClassName(parser_data.PluginName)
    context = {'plugin_name': parser_data.PluginName,
               'class_name': class_name,
               'queries': parser_data.Queries,
               'database_name': parser_data.DatabaseName,
               'required_tables': parser_data.RequiredTables}
    rendered = self.__helper.RenderTemplate(self._PARSER_TEMPLATE, context)
    return rendered
