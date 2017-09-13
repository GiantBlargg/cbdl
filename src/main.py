import click
from squif import SquiCol
from sites import siteHandle


@click.command()
@click.option("--dest", "-d", type=click.Path(file_okay=False), default=".")
@click.option(
	"--output", "-o", default="{{{series}}}/{{{title}}}.cbz/{{{name}}}.{{{ext}}}")
@click.argument("URL", nargs=-1, required=True)
def main(dest, output, url):
	col = SquiCol(dest, output)
	for u in url:
		siteHandle(u, col)
	col.close()
