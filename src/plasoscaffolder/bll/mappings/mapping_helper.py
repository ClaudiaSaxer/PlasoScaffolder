# -*- coding: utf-8 -*-
"""Helper methods for mapping."""
import jinja2

from plasoscaffolder.bll.mappings import base_mapping_helper
from plasoscaffolder.common import code_formatter


class MappingHelper(base_mapping_helper.BaseMappingHelper):
  """Mapping Helper class."""

  def __init__(self, template_path: str, yapf_path: str):
    """Initializing the mapping helper class.

    Args:
      template_path (str): the path to the template directory
      yapf_path (str): the path to the yapf path
    """
    super().__init__()
    template_loader = jinja2.FileSystemLoader(template_path)
    self._template_environment = jinja2.Environment(
        autoescape=False, loader=template_loader, trim_blocks=False)
    self.yapf_path = yapf_path

  def RenderTemplate(self, template_filename: str, context: dict) -> str:
    """Renders the template.

       Args:
         template_filename (str): the name of the template
         context (dict): the context of the template

       Returns:
         str: the rendered template
       """
    template = self._template_environment.get_template(
        template_filename).render(context)
    # Because jinja template variable is first escaped and then word wrapped,
    # the escaped backslash can be split and can result in an eol.
    # The escaped backslash will be placed on the next line.
    template = template.replace('\\\'\n        u\'\\','\'\n        u\'\\\\')

    formatter = code_formatter.CodeFormatter(self.yapf_path)

    formatted = formatter.Format(template)
    # Removing the yapf comment because it should not be in the resulting file.
    formatted_removed_yapf = formatted[0].replace(
        '# yapf: disable\n', '').replace('# yapf: enable\n', '').replace('  \n',
                                                                         '\n')
    return formatted_removed_yapf
    """return template"""

  def GenerateClassName(self, plugin_name: str) -> str:
    """Generates the class name from the plugin name.

    Args:
      plugin_name (str): the plugin name

    Returns:
      str: the class name
    """
    return plugin_name.replace('_', ' ').title().replace(' ', '')
