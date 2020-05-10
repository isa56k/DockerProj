#!/usr/bin/env python
import click

@click.command()
def hello():
    click.echo('Hellow World!')
    
if __name__ == '__main__':
    hello()