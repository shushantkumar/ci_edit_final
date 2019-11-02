from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timeit import timeit
import unittest

import app.parser


class pt7(unittest.TestCase):
    def testpt7(self):
        setup = '''def withDefault(a, b=None):\n'''
        setup += '''  if b is not None: return b\n'''
        setup += '''  return a*a\n'''
        setup += '''def withoutDefault(a, b):\n'''
        setup += '''  if b is -1: return b\n'''
        setup += '''  return a*b\n'''
        a = timeit('''withDefault(5);''' * 100, setup=setup, number=10000)
        b = timeit('''withoutDefault(5, 0);''' * 100, setup=setup, number=10000)
        # Assert that neither too much faster than the other
        self.assertGreater(a, b * 0.77)
        # This check is not performing the same in Python3.
        #self.assertGreater(b, a * 0.71)
