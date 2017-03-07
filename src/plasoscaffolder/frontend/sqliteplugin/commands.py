# -*- coding: utf-8 -*-
import click
from plasoscaffolder.frontend.controller.sqlite_controller import *

@click.command()
@click.option('--path', '-n', prompt="What's the path to the plaso project?",
              help='The path to plaso',callback=source_path)
@click.option('--name', '-n', prompt="What's the name of the plugin?",
              help='The plugin name',callback=plugin_name)
@click.option('--testfile', prompt="What's the path to your test file?",
              help='The testfile path',callback=test_path)

def sqlite(path, name, test_file):
  click.confirm('Do you want to generate the files?', abort=False)
  generate(path, name, test_file)