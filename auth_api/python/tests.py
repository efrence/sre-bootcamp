import unittest
from methods import Token, Restricted


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()
        # before header was {"alg": "HS256", "typ": "JWT"}
        # now after changes is {"typ": "JWT", "alg": "HS256"}
        # need it to play well with pyjwt library
        self.token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w'

    def test_generate_token(self):
        self.assertEqual(self.token, self.convert.generate_token('admin', 'secret'))

    def test_access_data(self):
        self.assertEqual('You are under protected data', self.validate.access_data(self.token))

if __name__ == '__main__':
    unittest.main()
