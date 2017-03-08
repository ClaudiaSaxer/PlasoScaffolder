# -*- coding: utf-8 -*-
""" Module representing function for the diffrent files """
from plasoscaffolder.bll.mappings.mapping_helper import render_template


def get_formatter_init_create(plugin_name):
  """
  renders formatter init if you want to create new init file
  :param plugin_name: the plugin name
  :return: string of the rendered template
  """
  file_name = "formatter_init_create_template.py"
  return _render_init(file_name, plugin_name)


def get_formatter_init_edit(plugin_name):
  """
  renders formatter init if you want to create new init file
  :param plugin_name: the plugin name
  :return: string of the rendered template
  """
  file_name = "formatter_init_edit_template.py"
  return _render_init(file_name, plugin_name)


def get_parser_init_create(plugin_name):
  """
  renders formatter init if you want to edit an existing init file
  :param plugin_name: the plugin name
  :return: string of the rendered template
  """
  file_name = "parser_init_create_template.py"
  return _render_init(file_name, plugin_name)


def get_parser_init_edit(plugin_name):
  """
  renders parser init if you want to create new init file
  :param plugin_name: the plugin name
  :return: string of the rendered template
  """
  file_name = "parser_init_edit_template.py"
  return _render_init(file_name, plugin_name)


def _render_init(file_name, plugin_name):
  """
  renders parser init if you want to edit an existing init file
  :param plugin_name: the plugin name
  :return: string of the rendered template
  """
  context = {'plugin_name': plugin_name}
  rendered = render_template(file_name, context)
  return rendered
