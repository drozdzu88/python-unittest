import unittest

class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertIn(2, [1, 2, 3, 4])

    def test_case_2(self):
        self.assertIn('@', 'example@example.com')

    def test_case_3(self):
        tech_stack = ['java', 'sql', 'python', 'aws']
        self.assertIn('python', tech_stack)

    def test_case_4(self):
        tech_stack = {'java': 'mid', 'python': 'senior'}
        self.assertIn('java', tech_stack)

    def test_case_5(self):
        tech_stack = {'java': 'mid', 'python': 'senior'}
        self.assertNotIn('c++', tech_stack)