# Czy poprawnie obliczany jest podatek
# czy poprawnie jest przypisana pensja po przyznaniu bonusu.

import unittest
from employe.emp import Employee

def setUpModule():
    print('setting up class...')
    global emp
    emp = Employee('John', 'Smith', 80000)

def tearDownModule():
    print('tearing down class...')
    global emp
    del emp

class TestEmployee(unittest.TestCase):

    def test_email_address(self):
        self.assertEqual(emp.email, 'john.smith@mail.com')

    def test_email_address_after_first_name_change(self):
        emp.first_name = 'Mike'
        self.assertEqual(emp.email, 'mike.smith@mail.com')

    def test_email_address_after_last_name_change(self):
        emp.last_name = 'Deep'
        self.assertEqual(emp.email, 'mike.deep@mail.com')

    def test_tax_amount(self):
        emp.salary = 80000
        self.assertEqual(emp.tax, 13600.0)

    def test_salary_after_bonus(self):
        emp.apply_bonus()
        self.assertEqual(emp.salary, 88000.0)