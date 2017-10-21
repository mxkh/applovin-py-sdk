import unittest

from request import Request


class TestRequest(unittest.TestCase):
    def test_columns_stringify(self):
        request = Request(
            'api key',
            '2017-09-20',
            '2017-09-20'
        )
        request.columns = ['day']
        self.assertEquals(len(request.columns), 1)


if __name__ == '__main__':
    unittest.main()
