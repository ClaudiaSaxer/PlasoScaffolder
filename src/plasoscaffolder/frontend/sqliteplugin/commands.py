# -*- coding: utf-8 -*-
"""The commands for the SQLite plugin."""
import os

import click
from plasoscaffolder.bll.services import sqlite_plugin_helper
from plasoscaffolder.common import output_handler_click
from plasoscaffolder.frontend.controller import sqlite_controller

# Since os.path.abspath() uses the current working directory (cwd)
# os.path.abspath(__file__) will point to a different location if
# cwd has been changed. Hence we preserve the absolute location of __file__.
__file__ = os.path.abspath(__file__)

Controller = sqlite_controller.SQLiteController(
    output_handler_click.OutputHandlerClick(),
    sqlite_plugin_helper.SQLitePluginHelper())


@click.command()
@click.option('--path', prompt='What\'s the path to the plaso project?',
              help='The path to plaso', callback=Controller.SourcePath)
@click.option('--name', prompt='What\'s the name of the plugin?',
              help='The plugin name', callback=Controller.PluginName)
@click.option('--testfile', prompt='What\'s the path to your test file?',
              help='The testfile path', callback=Controller.TestPath)
@click.option('--event',
              prompt='Please enter the main events of the plugin. [Event '
                     'Event ...]',
              help='The plugin events', callback=Controller.Event)
@click.option('--sql',
              prompt='What is your plugin SQL Query?',
              help='The SQL Query for the plugin.', callback=Controller.SQLQuery)
def sqlite(path, name, testfile, event, sql):
  template_path = os.path.join(
      os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
      'bll', 'templates')
  Controller.Generate(template_path)
