# -*- coding: utf-8 -*-
"""The start point of the plasoscaffolder."""
import click

from plasoscaffolder.frontend.sqliteplugin import commands as sqliteplugin


@click.group()
def entry_point():
  pass

#all plugin entrypoints for the scaffolder
entry_point.add_command(sqliteplugin.sqlite)

if __name__ == '__main__':
  entry_point()
