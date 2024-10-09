"""This module shows creation of commands using click
"""

import json
import click


@click.group()
def cli():
    """Cli entry point
    """
    pass


@cli.command()
@click.option('--file', 'file_path', required=True, type=click.Path(exists=True)
              , help="Path to the JSON file")
def read_json(file_path):
    """: Opens the JSON file and processes tasks

    Arguments:
        file_path -- The file path
    """
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    formatted_json = json.dumps(data, indent=4)
    click.echo(formatted_json)


@cli.command()
@click.option('--count', default =1, help='The number of greetings')
@click.argument('name')
def hello(count, name):
    """: Example script
    """
    for i in range(count):
        click.echo(f"Hello {name}!")
