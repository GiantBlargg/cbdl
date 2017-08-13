import click
from sites import siteHandle


@click.command()
@click.option("--archive-type","-t", type=click.Choice(["7","a","r","t","z"]), default="z")
@click.argument("URL")
def main(url):
	siteHandler(url)

