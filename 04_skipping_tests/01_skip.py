import unittest

class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('aws'.upper(), 'AWS')

# Skipp test using decorator @unittest.skip('reason'). We have to say the reason.
    @unittest.skip('Always skipping...')
    def test_case_2(self):
        self.assertEqual('aws'.upper(), 'AWS')
