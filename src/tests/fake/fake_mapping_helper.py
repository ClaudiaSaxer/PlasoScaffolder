# -*- coding: utf-8 -*-
"""fake for helper methods for mapping"""
from plasoscaffolder.bll.mappings.base_mapping_helper import BaseMappingHelper


class FakeMappingHelper(BaseMappingHelper):
  """Fake for the mapping helper."""

  def __init__(self, template_path: str):
    self.template_path = template_path

  def _get_template_environment(self):
    pass

  def render_template(self, template_filename: str, context: dict) -> str:
    return "fake string " + template_filename

  def generate_class_name(self, plugin_name: str) -> str:
    return "fake class name " + plugin_name
