from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User
# Create your tests here.
class TestAccountsForms(TestCase):
    
    def test_login_form(self):
        form = UserLoginForm({
            'username': 'admin',
            'password': 'pa55word'
        })
        self.assertTrue(form.is_valid())

    def test_login_password_required(self):
        form = UserLoginForm({'username': 'admin'})
        self.assertFalse(form.is_valid()) 
        self.assertEqual(form.errors['password'], ['This field is required.'])
        
        
    def test_login_username_required(self):
        form = UserLoginForm({'password': 'password'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])
        
    def test_registration_form(self):
        form = UserRegistrationForm({
            'username': 'admin',
            'email': 'adm@example.com',
            'password1': 'somepassword',
            'password2': 'somepassword'
        })
        self.assertTrue(form.is_valid())
        
        
        
    def test_registration_passwords_must_match(self):
        form = UserRegistrationForm({
            'username': 'admin',
            'email': 'adm@example.com',
            'password1': 'password1',
            'password2': 'password2',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ['Passwords do not match'])
        
    def test_registration_email_must_be_unique(self):
        User.objects.create_user(
            username= 'testuser',
            email='adm@example.com'
            )
  
        form = UserRegistrationForm({
            'username': 'admin',
            'email': 'adm@example.com',
            'password1': 'password1',
            'password2': 'password1',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Email addresses must be unique'])