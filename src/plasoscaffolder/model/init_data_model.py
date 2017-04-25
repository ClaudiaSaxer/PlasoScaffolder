# -*- coding: utf-8 -*-
"""The Init Data model class."""
from plasoscaffolder.model import base_data_model
from plasoscaffolder.model import sql_query_model


class InitDataModel(base_data_model.BaseDataModel):
  """Class for the data for the init template."""

  def __init__(self,
               plugin_name: str,
               is_create_template: bool):
    """Initialises the formatter data model.

    Args:
      plugin_name (str): the name of the plugin
      is_create_template (bool): true if it is a create template
    """
    super().__init__(plugin_name)
    self._is_create_template = is_create_template

  @property
  def IsCreateTemplate(self) -> bool:
    """If the template is a new file.

    Returns:
      bool: True if it is a create template
    """
    return self._is_create_template
