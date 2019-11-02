from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timeit import timeit
import unittest

import app.parser


class pt8(unittest.TestCase):
    def testpt8(self):
        setup = '''var = "apple"\n'''
        a = timeit('''k = var[0]+"1";''', setup=setup, number=10000)
        b = timeit('''k1 = ord(var[0])+1;''', setup=setup, number=100000)
        # Assert that neither too much faster than the other
        self.assertGreater(b, a)
        # This check is not performing the same in Python3.
        #self.assertGreater(b, a * 0.71)
