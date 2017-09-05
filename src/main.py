import click
from squif import SquiCol
from sites import siteHandle


@click.command()
@click.option("--dest", "-d", type=click.Path(file_okay=False), default=".")
@click.option("--archive-type","-t", type=click.Choice(["z"]), default="z")
@click.option("--output", "-o", default="${series}/${volume}/${chapter}-${title}")
@click.argument("URL", nargs=-1, required=True)
def main(dest, archive_type, output, url):
	col = SquiCol(dest, output)
	for u in url:
		siteHandle(u, col)
	col.close()

