
import click
import json

@click.group()
def cli():
    """Cli entry point
    """
    pass


@cli.command()
@click.option('--file', 'file_path', required=True, type=click.Path(exists=True)
              , help="Path to the JSON file")
def generate_python(file_path):
    """: Opens the JSON file and processes tasks

    Arguments:
        file_path -- The file path
    """
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    click.echo(data)

@cli.command()
@click.option('--count', default =1, help='The number of greetings')
@click.argument('name')
def hello(count, name):
    """: Example script
    """
    for i in range(count):
        click.echo(f"Hello {name}!")


