# -*- coding: utf-8 -*-
import click

from plasoscaffolder.frontend.sqliteplugin import commands as sqliteplugin


@click.group()
def entry_point():
  pass

entry_point.add_command(sqliteplugin.sqlite)

if __name__ == '__main__':
  entry_point()
