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


    #Boundary testing

    def test_boundary_diff(self):
        self.assertEqual(Methods.remainder(11, 1), 0)

    def test_boundary_divide(self):
        self.assertEqual(Methods.division(11, 1), 11)

    def test_power_base_boundary(self):
        self.assertEqual(Methods.power(0, 10), 0)

    def test_power_boundary(self):
        self.assertEqual(Methods.power(10, 0), 1)

    def test_power_from_file_base_boundary(self):
        Methods.writing_to_file("test_file.txt", 0, 10)
        self.assertEqual(Methods.power_from_file("test_file.txt"), 0)

    def test_power_from_file_power_boundary(self):
        Methods.writing_to_file("test_file.txt", 10, 0)
        self.assertEqual(Methods.power_from_file("test_file.txt"), 1)



    #Inverse testing

    def test_inverse_sum(self):
        expected_sum = Methods.sum(5,2)
        param1 = Methods.difference(Methods.sum(5,2), 2)
        self.assertEqual(param1, 5)

    def test_inverse_diff(self):
        # expected_diff = Methods.difference(10, 7)
        param1 = Methods.sum(Methods.difference(10, 7), 7)
        self.assertEqual(param1, 10)

    def test_inverse_remainder(self):
        remainder = Methods.remainder(10, 5)
        div = Methods.division(10, 5)
        self.assertEqual(div*5+remainder, 10)

    def test_inverse_divider(self):
        remainder = Methods.remainder(10,5)
        div = Methods.division(10, 5)
        self.assertEqual((10-remainder)/div, 5)

    def test_inverse_power(self):
        result = Methods.power(3, 4)
        for _ in range(3):
            result = result / 3
        self.assertEqual(result, 3)

    def test_inverse_power(self):
        Methods.writing_to_file("test_file.txt", 3, 4)
        result = Methods.power_from_file("test_file.txt")
        for _ in range(3):
            result = result / 3
        self.assertEqual(result, 3)


    #calculated by modulus
    def test_complex_inverse_sum(self):
        obj1 = Complex.Complex(-4, 5)
        obj2 = Complex.Complex(10, -2)
        sum = obj1 + obj2
        expected_param = (sum - obj2).fullnumber()
        self.assertEqual(expected_param, Complex.Complex(-4, 5).fullnumber())

    #calculated by modulus
    def test_complex_inverse_diff(self):
        obj1 = Complex.Complex(4, 7).modulus()
        obj2 = Complex.Complex(2, 10).modulus()
        diff = obj1 - obj2
        expected_param = obj1 - diff
        self.assertEqual(expected_param, Complex.Complex(2, 10).modulus())

    #rounding may be an issue here
    def test_complex_modulus_(self):
        obj = Complex.Complex(3, 4)
        result = obj.modulus()
        real = obj.real
        img = obj.img
        expected_param = math.ceil(math.sqrt(pow(result, 2) - pow(real, 2)))
        self.assertEqual(img, expected_param)


    #Cross-check testing

    def test_sorting_methods(self):
        list = Methods.random_list_generator(10)
        list_selection = Methods.selection_sort_list(list)
        list_quick = Methods.quick_sort_list(list)
        self.assertEqual(list_selection, list_quick, "Did not obtain the same result")


    #Error condition testing

    def test_error_remainder(self):
        self.assertRaises(Exception, Methods.remainder, 1, 0)
        # the_exception = context.exception
        # self.assertEqual("Divisor is less than 1" in context.exception)

    def test_error_divider(self):
        self.assertRaises(Exception, Methods.division, 10, 0)

    def test_error_phone_invalid(self):
        self.assertRaises(Exception, Methods.phoneValidator, +45223561)

    def test_error_power_overflow(self):                #too big number
        self.assertRaises(Exception, Methods.power, 10, 2222)

    def test_error_power_base_negative(self):
        self.assertRaises(Exception, Methods.power, -2, 5)

    def test_error_power_negative(self):
        self.assertRaises(Exception, Methods.power, 5, -3)

    def test_error_power_zero(self):
        self.assertRaises(Exception, Methods.power, 0, 0)

    def test_error_power_from_file_base_negative(self):
        Methods.writing_to_file("test_file.txt", -3, 5)
        self.assertRaises(Exception, Methods.power_from_file, "test_file.txt")

    def test_error_power_from_file_power_negative(self):
        Methods.writing_to_file("test_file.txt", 5, -1)
        self.assertRaises(Exception, Methods.power_from_file, "test_file.txt")

    def test_power_from_file_zero(self):
        Methods.writing_to_file("test_file.txt", 0, 0)
        self.assertRaises(Exception, Methods.power_from_file, "test_file.txt")

    def test_power_from_file_check_file_existence(self):
        self.assertRaises(Exception, Methods.power_from_file, "test_fileeeee.txt")

    def test_power_from_file_overflow(self):                #too big number
        Methods.writing_to_file("test_file.txt", 10, 2222)
        self.assertRaises(Exception, Methods.power_from_file, "test_file.txt")


    #Performance testing

    def test_performance_timing_sort(self):
        self.assertGreater(Methods.timer_function_quicksort(20), 0.00001)

    def test_performance_timing_quicksort(self):
        self.assertGreater(Methods.timer_function_selection_sort(20), 0.00001)


    # def test_error_file(self):
    #     self.assertEqual(RuntimeError, )



    #CORRECT principles

    # Conformance principle

    def test_conformance_sum(self):                         # ------ sum of integer numbers only
        self.assertIsInstance(Methods.sum(3, 5), int)

    def test_conformance_diff(self):                              # ----- diff of integer numbers only
        self.assertIsInstance(Methods.difference(5, 2), int)

    def test_conformance_remainder(self):                           # ------ remainder is rounded to int
        self.assertIsInstance(Methods.remainder(5, 1), int)

    def test_conformance_lower_bound(self):                         # ----- lowest element in list is bigger than 10  ---- if there was 10 instead of 9, sometimes the test would fail
        self.assertGreater(min(Methods.random_list_generator(10)), 9)

    def test_conformance_higher_bound(self):                        # ------ highest element in list is lower than 100 --- if there was 100 instead if 101, sometiems the test would fail
        self.assertGreater(101, max(Methods.random_list_generator(10)))

    def test_conformance_power(self):                               # ------ result is integer
        self.assertIsInstance(Methods.power(5, 3), int)

    def test_conformance_power_from_file(self):
        Methods.writing_to_file("test_file.txt", 4, 5)
        self.assertIsInstance(Methods.power_from_file("test_file.txt"), int)




if __name__ == '__main__':
    print("test")
    unittest.main()
