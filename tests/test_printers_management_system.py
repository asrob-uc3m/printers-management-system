import unittest

import printers_management_system


class Printers_management_systemTestCase(unittest.TestCase):

    def setUp(self):
        self.app = printers_management_system.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to Printers Management System', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
