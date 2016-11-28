import unittest


class UnderTest(object):
    def __init__(self):
        self.result = 0

    def sum(self, list):
        init = 0
        if len(list) > 0:
            for item in list:
                init += item
            self.result = init
            return self.result

    def multiplay(self, list):
        init = 1
        if len(list) > 0:
            for item in list:
                init *= item
            self.result = init
            return self.result


class BaseTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BaseTest, self).__init__(*args, **kwargs)
        self.underTest = UnderTest()

    # Test Case #1: Test integer list
    def test01_sum(self):
        list = [1, 2, 3]
        self.assertEqual(self.underTest.sum(list), 6)

    # Test Case #1: Test string list
    def test02_sum(self):
        list = ['apple', ' is', ' delicious.']
        self.assertEqual(self.underTest.sum(list), 'apple is delicious.')

    # Test Case #1: Test floating list
    def test03_sum(self):
        list = [1.23, 15246.123, 0.001]
        self.assertEqual(self.underTest.sum(list), 15247.354)

    # Test Case #1: Test empty list
    def test04_sum(self):
        list = []
        self.assertFalse(self.underTest.sum(list))

# You can use
suite = unittest.TestLoader().loadTestsFromTestCase(BaseTest)
unittest.TextTestRunner(verbosity=2).run(suite)

# OR
# if __name__ == '__main__':
#     unittest.main()