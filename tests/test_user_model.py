import unittest
from app.models.user import User


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(username='cat', password='p@assw0rd')
        self.assertTrue(u.password_hash is not None)

    def test_not_password_getter(self):
        u = User(username='cat', password='p@assw0rd')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(username='cat', password='p@assw0rd')
        self.assertTrue(u.verify_password('p@assw0rd'))
        self.assertFalse(u.verify_password('wrongp@assword'))

    def test_password_salts_are_random(self):
        u = User(username='cat', password='p@assw0rd')
        u2 = User(username='dog', password='p@assw0rd')
        self.assertTrue(u.password_hash != u2.password_hash)


