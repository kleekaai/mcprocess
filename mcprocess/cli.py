"""Console script for mcprocess."""
import sys
import click
import ntpath
import pandas as pd
from pathlib import Path
from utils import transform_data


@click.command()
@click.option(
    "--file", "-f", prompt="Enter the file path", help="Process file"
)
def main(file):
    """Process the file"""
    if file:
        click.echo("Parsing file")
        processed_file_name = ntpath.basename(
            file).split(".")[0] + "_processed.csv"
        df = pd.read_csv(file, error_bad_lines=False)
        df = transform_data(df)
        df.to_csv(base_dir / processed_file_name, sep=",", index=False)
        click.echo("Generated processed file.")
        # click.echo('{0}, {1}.'.format(greet, name))


if __name__ == "__main__":
	base_dir = Path.cwd()
	sys.exit(main())