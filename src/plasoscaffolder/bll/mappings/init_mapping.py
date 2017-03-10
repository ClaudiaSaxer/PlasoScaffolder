# -*- coding: utf-8 -*-
""" Module representing function for the different files """
from plasoscaffolder.bll.mappings.mapping_helper import  MappingHelper


class InitMapper(object):
  """class representing the init mapper"""

  def __init__(self, template_path:str):
    """Initializing the init mapper class

    Args:
      template_path: the path to the template directory
    """
    super(InitMapper, self).__init__()
    self.helper = MappingHelper(template_path)

  def get_formatter_init_create(self, plugin_name: str) -> str:
    """renders formatter init if you want to create new init file

    Args:
      plugin_name: the plugin name

    Returns: string of the rendered template
    """
    file_name = "formatter_init_create_template.py"
    return self._render_init(file_name, plugin_name)


  def get_formatter_init_edit(self, plugin_name: str) -> str:
    """renders formatter init if you want to create new init file

    Args:
      plugin_name: the plugin name

    Returns: string of the rendered template
    """
    file_name = "formatter_init_edit_template.py"
    return self._render_init(file_name, plugin_name)


  def get_parser_init_create(self, plugin_name: str) -> str:
    """renders formatter init if you want to edit an existing init file

    Args:
      plugin_name: the plugin name

    Returns: string of the rendered template
    """
    file_name = "parser_init_create_template.py"
    return self._render_init(file_name, plugin_name)


  def get_parser_init_edit(self, plugin_name: str) -> str:
    """renders parser init if you want to create new init file

    Args:
      plugin_name: the plugin name

    Returns: string of the rendered template
    """
    file_name = "parser_init_edit_template.py"
    return self._render_init(file_name, plugin_name)


  def _render_init(self, file_name: str, plugin_name: str) -> str:
    """renders parser init if you want to edit an existing init file

    Args:
      file_name: name of the file in the templates folder
      plugin_name: the name of the plugin

    Returns:string of the rendered template
    """
    context = {'plugin_name': plugin_name}
    rendered = self.helper.render_template(file_name, context)
    return rendered
