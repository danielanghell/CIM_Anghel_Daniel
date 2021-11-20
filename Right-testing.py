import unittest
import Complex
import Methods
import math
import random
import os

class MyTestCase(unittest.TestCase):

    #RIGHT principle
    def test_sum(self):
        self.assertEqual(Methods.sum(6, 11), 17)

    def test_diff(self):
        self.assertEqual(Methods.difference(10, 6), 4)

    def test_remainder(self):
        self.assertEqual(Methods.remainder(10, 3), 1)

    def test_power(self):
        self.assertEqual(Methods.power(3, 4), 81)

    def test_power_from_file(self):
        Methods.writing_to_file("test_file.txt", 3, 4)
        self.assertEqual(Methods.power_from_file("test_file.txt"), 81)

    def test_divide(self):
        self.assertEqual(Methods.division(120, 5), 24)

    def test_phoneValidator(self):
        self.assertEqual(Methods.phoneValidator("+40775315489"), True)

    def test_rangedListFabric(self):
        expected_result = len(Methods.rangedListFabric(4))
        self.assertEqual(expected_result, 4)

    def test_selection_sort(self):                          # ------- also as Ordering principle from CORRECT
        expected_list = Methods.random_generator_and_selection_sort(5)
        ok = False
        for i in range(len(expected_list)-1):
            if expected_list[i] > expected_list[i+1]:
                ok = True
        self.assertEqual(False, ok, "List is not sorted")

    def test_quick_sort(self):                              # ------- also as Ordering principle from CORRECT
        expected_list = Methods.random_generator_and_quicksort(8)
        ok = False
        for i in range(len(expected_list)-1):
            if expected_list[i] > expected_list[i+1]:
                ok = True
        self.assertEqual(False, ok, "List is not sorted")

    def test_random_list_generator(self):
        list = Methods.random_list_generator(10)
        ok = True
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                ok = False
        self.assertEqual(False, ok, "List was generated already sorted")

    def test_complex_sum(self):
        self.assertEqual(Complex.sumComplex_numbers(Complex.Complex(2, 4), Complex.Complex(3, 1)), Complex.Complex(5,5).fullnumber(), "Not equal sum")

    def test_complex_difference(self):
        self.assertEqual(Complex.subComplex_numbers(Complex.Complex(2, 10), Complex.Complex(4, -10)), Complex.Complex(-2,20).fullnumber(), "Not equal difference")

    def test_complex_modulus(self):
        self.assertEqual(Complex.modulusComplex_numbers(), 6, "Not equal modulus of complex number")
