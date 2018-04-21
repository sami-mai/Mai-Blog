
from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import User, Role, Subscriber, BlogPost, Category, Comment

# Creating app instance
app = create_app('default')
# app = create_app('test')
# app = create_app('production')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
manager.add_command('server', Server)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Subscriber=Subscriber, BlogPost=BlogPost, Category=Category, Comment=Comment)


if __name__ == '__main__':
    manager.run()
