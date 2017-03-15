# -*- coding: utf-8 -*-
"""The commands for the SQLite plugin."""
import os

import click
from plasoscaffolder.common.output_handler_click import OutputHandlerClick
from plasoscaffolder.frontend.controller.sqlite_controller import \
  SQLiteController

# Since os.path.abspath() uses the current working directory (cwd)
# os.path.abspath(__file__) will point to a different location if
# cwd has been changed. Hence we preserve the absolute location of __file__.
__file__ = os.path.abspath(__file__)

controller = SQLiteController(OutputHandlerClick())


@click.command()
@click.option('--path', prompt='What\'s the path to the plaso project?',
  help='The path to plaso', callback=controller.source_path)
@click.option('--name', prompt='What\'s the name of the plugin?',
  help='The plugin name', callback=controller.plugin_name)
@click.option('--testfile', prompt='What\'s the path to your test file?',
  help='The testfile path', callback=controller.test_path)
@click.option('--event', prompt='Please enter the main events of the plugin. [event event ...]',
  help='The plugin events', callback=controller.event)
def sqlite(path, name, testfile, event):
  template_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    'bll', 'templates')
  controller.generate(template_path)
