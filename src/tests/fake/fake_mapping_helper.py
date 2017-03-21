# -*- coding: utf-8 -*-
"""fake for helper methods for mapping"""
from plasoscaffolder.bll.mappings.base_mapping_helper import BaseMappingHelper


class FakeMappingHelper(BaseMappingHelper):
  """Fake for the mapping helper."""

  def __init__(self, template_path: str):
    self.template_path = template_path

  def _GetTemplateEnvironment(self):
    pass

  def RenderTemplate(self, template_filename: str, context: dict) -> str:
    return "fake string " + template_filename

  def GenerateClassName(self, plugin_name: str) -> str:
    return "fake class name " + plugin_name
