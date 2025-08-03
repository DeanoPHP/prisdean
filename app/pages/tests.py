from django.test import SimpleTestCase
from django.urls import reverse


class Test_homepage(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'pages/index.html')
        
    def test_homepage_has_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Home page')