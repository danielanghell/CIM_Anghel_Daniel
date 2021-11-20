
import unittest
import Complex
import Methods
import math
import random
import os

class MyTestCase(unittest.TestCase):


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
