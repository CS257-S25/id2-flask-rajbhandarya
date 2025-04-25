''' Test the Flask app routes and error handlers.'''
import unittest
from app import app, get_data

class TestHomePage(unittest.TestCase):
    ''' Testing the homepage'''
    def test_route(self):
        ''' Test the homepage route '''
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        homepage_text_str = ("Hello, this is the homepage. To find a random recipe, "
                              "go type /number after the current URL where number "
                              "is the amount of random recipes you want.")
        homepage_text_bytes = homepage_text_str.encode('utf-8')
        self.assertIn(homepage_text_bytes, response.data)

class TestGetRandom(unittest.TestCase):
    ''' Testing the get random capability'''
    def test_route(self):
        ''' Test the get_random route '''
        self.app = app.test_client()
        response = self.app.get('/1', follow_redirects=True)
        data = get_data()
        random = (' - '.join(map(str, data[9220]))).encode('utf-8')
        self.assertEqual(random, response.data)

class TestRoute404(unittest.TestCase):
    ''' Testing the 404 error handler'''
    def test_route_404(self):
        ''' Test the 404 error handler '''
        self.app = app.test_client()
        response = self.app.get('/0/1/2', follow_redirects=True)
        self.assertEqual(b'Sorry, wrong format. Type /number after the current URL.', response.data)

class TestRoute500(unittest.TestCase):
    ''' Testing the 500 error handler'''
    def test_route_500(self):
        ''' Test the 500 error handler '''
        self.app = app.test_client()
        response = self.app.get('/a', follow_redirects=True)
        self.assertEqual(b'Eek, a bug!', response.data)

if __name__ == '__main__':
    unittest.main()
