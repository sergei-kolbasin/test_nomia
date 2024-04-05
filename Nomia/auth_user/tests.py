from django.test import TestCase
from django.urls import reverse


class LoginViewTestCase(TestCase):
    def test_get_request_authenticated_user(self):
        response = self.client.get(reverse('auth_user:login_view'))
        self.assertEqual(response.status_code, 302)

    def test_post_request_invalid_credentials(self):
        response = self.client.post(reverse('login_view'), {'username': 'invalid_user', 'password': 'invalid_password'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid username or password. Please try again.")
