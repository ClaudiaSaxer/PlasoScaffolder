import click 

from sqliteplugin import commands as sqliteplugin
from tempplugin import commands as tempplugin

@click.group()
def entry_point():
    pass

entry_point.add_command(tempplugin.temp)
entry_point.add_command(sqliteplugin.sqlite)

if __name__ == '__main__':
    entry_point()
