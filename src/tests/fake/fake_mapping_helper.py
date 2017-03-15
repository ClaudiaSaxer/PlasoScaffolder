# -*- coding: utf-8 -*-
"""Helper methods for mapping"""
from plasoscaffolder.bll.mappings.base_mapping_helper import BaseMappingHelper


class FakeMappingHelper(BaseMappingHelper):

  def __init__(self, template_path: str):
    self.template_path = template_path

  def _get_template_environment(self):
    pass

  def render_template(self, template_filename: str, context: dict) -> str:
    return "fake string "+template_filename
