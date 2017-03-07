# -*- coding: utf-8 -*-

from plasoscaffolder.frontend.controller.sqlite_controller import *
import click

controller = SqliteController()

@click.command()
@click.option('--path', '-p', prompt="What's the path to the plaso project?",
  help='The path to plaso', callback=controller.source_path)
@click.option('--name', prompt="What's the name of the plugin?",
  help='The plugin name', callback=controller.plugin_name)
@click.option('--testfile', prompt="What's the path to your test file?",
  help='The testfile path', callback=controller.test_path)
def sqlite(path, name, testfile):
  click.confirm('Do you want to generate the files?', abort=True, default=True)
  controller.generate(path, name, testfile)
