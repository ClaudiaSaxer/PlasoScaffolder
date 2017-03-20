# -*- coding: utf-8 -*-
""" fake for module representing function for the different files """
from plasoscaffolder.bll.mappings.base_init_mapping import BaseInitMapper
from plasoscaffolder.bll.mappings.base_mapping_helper import BaseMappingHelper


class FakeInitMapper(BaseInitMapper):
  """class representing the init mapper"""

  def __init__(self, template_path: str, mapping_helper: BaseMappingHelper):
    pass

  def get_formatter_init_create(self, plugin_name: str) -> str:
    return plugin_name

  def get_formatter_init_edit(self, plugin_name: str) -> str:
    return plugin_name

  def get_parser_init_create(self, plugin_name: str) -> str:
    return plugin_name

  def get_parser_init_edit(self, plugin_name: str) -> str:
    return plugin_name

  def _render_init(self, file_name: str, plugin_name: str) -> str:
    return plugin_name
