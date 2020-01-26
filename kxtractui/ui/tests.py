from django.test import TestCase

# Create your tests here.

class HomePageTest(TestCase):

    def test_episodes_redirectl(self):
        response = self.client.get("/ui/episodes")
        self.assertEqual(response.get('location'), '/ui/episodes/')

    def test_episodes_empty_return_correct_html(self):
        response = self.client.get("/ui/episodes", follow=True)
        self.assertTemplateUsed(response, "episodes/index.html")
        html = response.content.decode('utf8')
        self.assertIn('No episodes are available', html)
