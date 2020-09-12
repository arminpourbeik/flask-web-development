import os

from flask_migrate import Migrate

from app import create_app, db
from app.models.user import User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app=app, db=db)


@app.cli.command()
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames('test_names')
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)
