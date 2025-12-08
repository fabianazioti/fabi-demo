from pathlib import Path
from time import sleep

import click
from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    TextColumn,
    TimeRemainingColumn,
    SpinnerColumn,
)

from .fabi_demo import DEMO


class Config:
    """A simple decorator class for command line options."""

    def __init__(self):
        """Initialization of Config decorator."""


pass_config = click.make_pass_decorator(Config, ensure=True)

console = Console()


@click.group()
@click.version_option()
@pass_config
def cli(config):
    """Mosaic Utilities on command line."""


@cli.command()
@click.argument(
    "input_dir",
    type=click.Path(exists=True, writable=False, readable=True, path_type=Path),
)
@pass_config
def reescale(config: Config, input_dir):
    """Reescale datadir INPUT_DIR.

    INPUT_DIR is the directory of the files.
    """
    print(input_dir)
