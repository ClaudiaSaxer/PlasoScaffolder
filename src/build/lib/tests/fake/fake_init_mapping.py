# -*- coding: utf-8 -*-
""" fake for module representing function for the different files """
from plasoscaffolder.bll.mappings import base_init_mapping
from plasoscaffolder.bll.mappings import base_mapping_helper


class FakeInitMapper(base_init_mapping.BaseInitMapper):
  """class representing the init mapper"""

  def __init__(self, template_path: str,
               mapping_helper: base_mapping_helper.BaseMappingHelper):
    pass

  def GetFormatterInitCreate(self, plugin_name: str) -> str:
    return plugin_name

  def GetFormatterInitEdit(self, plugin_name: str) -> str:
    return plugin_name

  def GetParserInitCreate(self, plugin_name: str) -> str:
    return plugin_name

  def GetParserInitEdit(self, plugin_name: str) -> str:
    return plugin_name

  def _RenderInit(self, file_name: str, plugin_name: str) -> str:
    return plugin_name
