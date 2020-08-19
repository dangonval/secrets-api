import click
from flask.cli import FlaskGroup

from secrets_api.app import create_app


def create_secrets_api(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_secrets_api)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Create a new admin user
    """
    from secrets_api.extensions import db
    from secrets_api.models import User

    click.echo("create user")
    user = User(username="admin", email="admin@mail.com", password="admin", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()
