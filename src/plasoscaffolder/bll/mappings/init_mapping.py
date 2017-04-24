# -*- coding: utf-8 -*-
"""Class representing the mapper for the init files."""
from plasoscaffolder.bll.mappings import base_init_mapping
from plasoscaffolder.bll.mappings import base_mapping_helper


class InitMapper(base_init_mapping.BaseInitMapper):
  """Class representing the init mapper."""

  _FORMATTER_INIT_CREATE_TEMPLATE = 'formatter_init_create_template.jinja2'
  _FORMATTER_INIT_EDIT_TEMPLATE = 'formatter_init_edit_template.jinja2'
  _PARSER_INIT_CREATE_TEMPLATE = 'parser_init_create_template.jinja2'
  _PARSER_INIT_EDIT_TEMPLATE = 'parser_init_edit_template.jinja2'

  def __init__(self, mapping_helper: base_mapping_helper.BaseMappingHelper()):
    """Initializing the init mapper class.

    Args:
      mapping_helper (base_mapping_helper.BaseMappingHelper): the helper class
          for the mapping
    """
    super().__init__()
    self.__helper = mapping_helper

  def GetFormatterInitCreate(self, plugin_name: str) -> str:
    """Renders formatter init if you want to create new init file.

    Args:
      plugin_name (str): the plugin Name

    Returns:
      str: the rendered template
    """
    return self._RenderInit(self._FORMATTER_INIT_CREATE_TEMPLATE, plugin_name)

  def GetFormatterInitEdit(self, plugin_name: str) -> str:
    """Renders formatter init if you want to create new init file.

    Args:
      plugin_name (str): the plugin Name

    Returns:
       str: the rendered template
    """
    return self._RenderInit(self._FORMATTER_INIT_EDIT_TEMPLATE, plugin_name)

  def GetParserInitCreate(self, plugin_name: str) -> str:
    """Renders formatter init if you want to edit an existing init file.

    Args:
      plugin_name (str): the plugin Name

    Returns:
       str: the rendered template
    """
    return self._RenderInit(self._PARSER_INIT_CREATE_TEMPLATE, plugin_name)

  def GetParserInitEdit(self, plugin_name: str) -> str:
    """Renders parser init if you want to create new init file.

    Args:
      plugin_name (str): the plugin Name

    Returns:
       str: the rendered template
    """
    return self._RenderInit(self._PARSER_INIT_EDIT_TEMPLATE, plugin_name)

  def _RenderInit(self, file_name: str, plugin_name: str) -> str:
    """Renders parser init if you want to edit an existing init file.

    Args:
      file_name (str): Name of the file in the templates folder
      plugin_name (str): the Name of the plugin

    Returns:
       str: the rendered template
    """
    context = {'plugin_name': plugin_name}
    rendered = self.__helper.RenderTemplate(file_name, context)
    return rendered
