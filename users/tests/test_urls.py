from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import TwoFactorAuthStatus


class TestUrls(SimpleTestCase):

    def test_two_fa_status_is_resolved(self):
        url = reverse('twofa_status')
        self.assertEqual(resolve(url).func.view_class, TwoFactorAuthStatus)