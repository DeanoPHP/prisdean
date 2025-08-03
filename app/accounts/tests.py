from django.test import TestCase
from accounts.models import CustomUser


class CustomUserTests(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            username='jon',
            email='jon@gmail.com',
            password='testpassword'
        )
        self.assertEqual(user.email, 'jon@gmail.com')
        self.assertTrue(user.check_password, 'testpassword')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_authenticated)      

    def create_super_user(self):
        user = CustomUser.objects.create_superuser(
            username='dean',
            email='deanolark@gmail.com',
            password='test'
        )
        self.assertEqual(user.username, 'dean')
        self.assertEqual(user.email, 'deanolark@gmail.com')
        self.assertEqual(user.password, 'test')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
