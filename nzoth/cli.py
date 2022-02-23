import click

from nzoth.utils.config import Config
from nzoth.utils.template import Template

@click.command()
@click.option('--config-file', help="YAML Config File")
def create(config_file):
    config = Config.load(config_file)
    Template.render(config)

if __name__ == "__main__":
    create()