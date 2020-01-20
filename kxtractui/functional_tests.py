from selenium import webdriver
import unittest


class BasicSmokeTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_podcasts_title(self):
		self.browser.get('http://localhost:8000/ui/podcasts/')
		self.assertIn('Podcast List', self.browser.title)

	def test_episodes_title(self):
		self.browser.get('http://localhost:8000/ui/episodes/')
		self.assertIn('Episode List', self.browser.title)


if __name__ == '__main__':
	unittest.main(warnings='ignore')
