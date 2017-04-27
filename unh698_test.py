import unittest

import unh698


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = unh698.app.test_client()

    def tearDown(self):
        pass

    def test_home_page(self):
        # Render the / path of the website
        rv = self.app.get('/')
        # Chech that the page contians the desired phrase
        assert b'UNH698 Website' in rv.data

    def test_home_Page(self):
        rv = self.app.get('/')
        #search the page contents for the link to your topic
        #replace xxxxxxx with text you expect tp see on main page that links to subpage
        assert b'Collecting' in rv.data

    def test_topic_page(self):
        rv = self.app.get('/my-topic')    
        assert b'Football Cards!' in rv.data
if __name__ == '__main__':
    unittest.main()