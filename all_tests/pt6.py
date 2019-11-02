from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timeit import timeit
import unittest

import app.parser


class pt6(unittest.TestCase):
    def testpt6(self):
        setup = '''x = [['a' * 100]*100]*100\n'''
        a = timeit('''x[0][0][0][:2] == "  "\n''', setup=setup, number=100000)
        b = timeit('''x[0][0][0].startswith("  ")\n''', setup=setup, number=100000)
        c = timeit(
            '''x[0][0][0] == " " and x[0][0][1] == " "\n''', setup=setup, number=100000)
        #print("\na %s, b %s, c %s | %s %s" % (a, b, c, c, a/c))
        # Calling a function or member is significantly slower than direct
        # access.

        # This check is not performing the same in Python3.
        self.assertGreater(b, a * 0.2)  # b is much slower.
        self.assertGreater(b, c * 0.2)  # b is much slower.
        self.assertGreater(a, c * 0.6)  # a and c are similar.
        self.assertGreater(c, a * 0.4)  # a and c are similar.