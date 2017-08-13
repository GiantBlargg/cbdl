import click
from squif import SquiCol
from sites import siteHandle


@click.command()
@click.option("--dest", "-d", type=click.Path(file_okay=False), default=".")
@click.option("--archive-type","-t", type=click.Choice(["7","a","r","t","z"]), default="z")
@click.option("--output", "-o", default="${series}/${volume}/${chapter}-${title}")
@click.argument("URL")
def main(dest, archive_type, output, url):
	siteHandle(url, SquiCol(dest, output))

