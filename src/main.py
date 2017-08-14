import click
from squif import SquiCol
from sites import siteHandle


@click.command()
@click.option("--dest", "-d", type=click.Path(file_okay=False), default=".")
@click.option("--archive-type","-t", type=click.Choice(["z"]), default="z")
@click.option("--output", "-o", default="${series}/${volume}/${chapter}-${title}")
@click.argument("URL")
def main(dest, archive_type, output, url):
	col = SquiCol(dest, output)
	siteHandle(url, col)
	col.close()

