# -*- coding: utf-8 -*-
""" Module representing function for the different files. """
from plasoscaffolder.bll.mappings import base_mapping_helper
from plasoscaffolder.bll.mappings import base_parser_mapping
from plasoscaffolder.model import sql_query_model


class ParserMapper(base_parser_mapping.BaseParserMapper):
  """Class representing the parser mapper."""

  _PARSER_TEMPLATE = 'parser_template.jinja2'

  def __init__(self, mapping_helper: base_mapping_helper.BaseMappingHelper()):
    """Initializing the init mapper class.

    Args:
      template_path (str): the path to the template directory
    """
    super().__init__()
    self.__helper = mapping_helper

  def GetParser(self, plugin_name: str, events: list, queries: [sql_query_model.SQLQueryModel]) -> str:
    """Retrieves the parser.

    Args:
      plugin_name (str): the name of the plugin
      events (list): the list of the events
      queries ([sql_query_model.SQLQueryModel]): list of queries

    Returns:
      str: the rendered template
    """
    class_name = self.__helper.GenerateClassName(plugin_name)
    context = {'plugin_name': plugin_name, 'class_name': class_name,
               '__events': events, 'queries':queries}
    rendered = self.__helper.RenderTemplate(self._PARSER_TEMPLATE, context)
    return rendered
