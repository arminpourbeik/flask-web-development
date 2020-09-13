import unittest

from app.models.user import User, Permission, AnonymousUser
from app.models.role import Role

from app import create_app, db


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        u = User(username='cat', password='p@assw0rd', email='cat@gmail.com')
        self.assertTrue(u.password_hash is not None)

    def test_not_password_getter(self):
        u = User(username='cat', email='cat@gmail.com', password='p@assw0rd')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(username='cat', email='cat@gmail.com', password='p@assw0rd')
        self.assertTrue(u.verify_password('p@assw0rd'))
        self.assertFalse(u.verify_password('wrongp@assword'))

    def test_password_salts_are_random(self):
        u = User(username='cat', password='p@assw0rd', email='cat@gmail.com')
        u2 = User(username='dog', password='p@assw0rd', email='cat2@gmail.com')
        self.assertTrue(u.password_hash != u2.password_hash)

    def test_user_role(self):
        u = User(username='john', email='john@example.com', password='cat')
        self.assertTrue(u.can(Permission.FOLLOW))
        self.assertTrue(u.can(Permission.COMMENT))
        self.assertTrue(u.can(Permission.WRITE))
        self.assertFalse(u.can(Permission.MODERATE))
        self.assertFalse(u.can(Permission.ADMIN))

    def test_moderator_role(self):
        r = Role.query.filter_by(name='Moderator').first()
        u = User(username='john', email='john@example.com', password='cat', role=r)
        self.assertTrue(u.can(Permission.FOLLOW))
        self.assertTrue(u.can(Permission.COMMENT))
        self.assertTrue(u.can(Permission.WRITE))
        self.assertTrue(u.can(Permission.MODERATE))
        self.assertFalse(u.can(Permission.ADMIN))

    def test_administrator_role(self):
        r = Role.query.filter_by(name='Administrator').first()
        u = User(username='john', email='john@example.com', password='cat', role=r)
        self.assertTrue(u.can(Permission.FOLLOW))
        self.assertTrue(u.can(Permission.COMMENT))
        self.assertTrue(u.can(Permission.WRITE))
        self.assertTrue(u.can(Permission.MODERATE))
        self.assertTrue(u.can(Permission.ADMIN))

    def test_anonymous_user(self):
        u = AnonymousUser()
        self.assertFalse(u.can(Permission.FOLLOW))
        self.assertFalse(u.can(Permission.COMMENT))
        self.assertFalse(u.can(Permission.WRITE))
        self.assertFalse(u.can(Permission.MODERATE))
        self.assertFalse(u.can(Permission.ADMIN))


