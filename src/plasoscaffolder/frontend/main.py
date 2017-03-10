# -*- coding: utf-8 -*-
"""The start point of the plasoscaffolder"""
import click
import os
from plasoscaffolder.frontend.sqliteplugin import commands as sqliteplugin


@click.group()
def entry_point():
  pass

entry_point.add_command(sqliteplugin.sqlite)

if __name__ == '__main__':
  entry_point()