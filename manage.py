from flask_script import Manager, Server
from app import create_app
import os

config_name = os.environ.get("Flask_config", "development")
app = create_app()
manage = Manager(app)
manage.add_command("runserver", Server(use_debugger=True))

if __name__ == '__main__':
    manage.run()
