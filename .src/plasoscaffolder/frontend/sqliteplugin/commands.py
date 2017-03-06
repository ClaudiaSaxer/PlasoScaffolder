# -*- coding: utf-8 -*-
import click

from .controller import sourcepath,pluginname,testpath

@click.command()
@click.option('--path', '-n', prompt="What's the path to the plaso project?",
              help='The path to plaso',callback=sourcepath)
@click.option('--name', '-n', prompt="What's the name of the plugin?",
              help='The plugin name',callback=pluginname)
@click.option('--testfile', prompt="What's the path to your test file?",
              help='The testfile path',callback=testpath)

def sqlite(path,name,testfile):
  click.confirm('Do you want to generate the files?', abort=False)
  
    

