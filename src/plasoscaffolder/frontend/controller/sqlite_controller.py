# -*- coding: utf-8 -*-
"""File representing the controller for sqLite plugin"""
import os

from plasoscaffolder.bll.services.file_creator import *
import click
from plasoscaffolder.bll.services.sqlite_plugin_helper import *


class SqliteController:
  path = None
  name = None

  def source_path(self, ctx, param, value):
    """save the source path"""
    print("save source path " + value)
    self.path = value
    return value

  def plugin_name(self, ctx, param, value):
    """save the plugin name"""
    print("save plugin name " + value)
    while plugin_exists(self.path, value):
      value = click.prompt("Plugin exists. Choose new name: ")
    self.name = value
    return value

  def test_path(self, ctx, param, value):
    """save the path"""
    print("save test path " + value)
    return value

  def generate(self, path, name, testfile):
    """generate files"""
    creator = FileCreator()
    file = creator.create_file_from_path

    print("generate " + file(formatter_file_path(path, name)))
    print("generate " + file(parser_file_path(path, name)))
    print("generate " + file(parser_test_file_path(path, name)))
    print("generate " + file(formatter_test_file_path(path, name)))

  print("Generate")
