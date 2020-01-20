from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_title(self):
		self.browser.get('http://localhost:8000/ui/podcasts/index.html')
		self.assertIn('Podcast List', self.browser.title)


if __name__ == '__main__':
	unittest.main(warnings='ignore')
