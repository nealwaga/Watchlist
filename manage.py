from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Role
from flask_migrate import Migrate, MigrateCommand

#Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

#@manage.shell decorator to create a shell context and the make_shell_context function allows us to pass in some properties into our shell. We return the app application instance, db database instance and the User class.
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Role = Role)

if __name__ == '__main__':
    manager.run()

#@manager.command

# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)
