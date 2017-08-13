import click
import re

@click.command()
@click.option("--archive-type","-t", type=click.Choice(["7","a","r","t","z"]), default="z")
@click.argument("URL")
def main(url):
	m=re.match("^(?:(.*):\/\/)?([a-zA-Z0-9-\.]+\.[a-zA-Z0-9-]+)(?:\/(.*))?$", url)
	if(m==None):
		print("Invalid URL")
		exit(1)

	if(m.group(2)!="dynasty-scans.com"):
		print(m.group(2)+" is not supported.")
		exit(1)

