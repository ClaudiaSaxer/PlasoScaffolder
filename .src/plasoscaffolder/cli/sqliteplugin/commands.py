import click

def events(ctx,param,value):
  for x in range(value):
    value = click.prompt('Enter the query for the'+str(x), default=12)
    click.echo(value)

@click.command()
@click.option('--name', '-n', prompt="What's the name of the plugin?",
              help='The plugin name')
@click.option('--tfp', prompt="What's the path to your test file?",
              help='The testfile path')
@click.option('--tables', prompt="What tables need to exist in the database?",
              help='database tables')
@click.option('--event', default=3, prompt="Which different event types do you have?",
              help='event types',callback=events)
@click.option('--testfile', prompt="What's the path to your test file?",
              help='The testfile path')
def sqlite(name,tfp,tables,event,testfile):
  click.confirm('Do you want to generate the files?', abort=False)
  click.echo("generated")
  click.echo(name)
  click.echo(tfp)
  click.echo(tables)
  click.echo(event)
  click.echo(testfile)

    

