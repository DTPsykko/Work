import unittest
TestingMain = __import__("Exercise-TestingMain")


class TestMain(unittest.TestCase):
    def setUp(self):
        print('Starting')

    def test_input(self):
        answer = 5
        guess = 5
        result = TestingMain.run_guess(answer, guess)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
