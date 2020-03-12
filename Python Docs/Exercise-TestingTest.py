import unittest
TestingMain = __import__('Exercise-TestingMain')


class TestMain(unittest.TestCase):
    def setUp(self):
        print('Starting')

    def test_input(self):
        result = TestingMain.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = TestingMain.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = TestingMain.run_guess(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = TestingMain.run_guess(5, '11')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
