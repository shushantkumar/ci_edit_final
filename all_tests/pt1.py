from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timeit import timeit
import unittest

import app.parser


class pt1(unittest.TestCase):

    def testpt1(self):
        setup = '''data = ['a'] * 100\n'''
        setup += '''def get(n):\n'''
        setup += '''  return data[n]\n'''
        setup += '''class B:\n'''
        setup += '''  def getViaMember(self, n):\n'''
        setup += '''    return data[n]\n'''
        setup += '''  def __getitem__(self, n):\n'''
        setup += '''    return data[n]\n'''
        setup += '''b = B()\n'''
        a = timeit('''x = data[5]\n''', setup=setup, number=10000)
        b = timeit('''x = get(5)\n''', setup=setup, number=10000)
        c = timeit('''x = b.getViaMember(5)\n''', setup=setup, number=10000)
        d = timeit('''x = b[5]\n''', setup=setup, number=10000)
        #print("\n%s | %s %s | %s %s | %s %s" % (a, b, a/b, c, a/c, d, a/d))
        # Calling a function or member is significantly slower than direct
        # access.
        self.assertGreater(b, a * 1.5)
        self.assertGreater(c, a * 2)
        self.assertGreater(d, a * 2)