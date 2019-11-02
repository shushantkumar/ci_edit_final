from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timeit import timeit
import unittest

import app.parser


class pt13(unittest.TestCase):
    def testpt13(self):
        # This tests a performance assumption. If this test fails, the
        # program should still work fine, but it may not run as fast as it
        # could by using different assumptions.
        #
        # With frequent splitting the performance reverses.
        for lineCount in (100, 1000, 5000):
            half = lineCount // 2
            a = timeit(
                r'''data2 = data1.split('\n'); \
            data2[%s] = data2[%s][:50] + "x" + data2[%s][50:]; \
            ''' % (half, half, half),
                setup=r'''data1 = ("a" * 100 + '\n') * %s''' % (lineCount,),
                number=10000)
            b = timeit(
                'data1 = data1[:%s] + "x" + data1[%s:]' % (half, half),
                setup=r'''data1 = ("a" * 100 + '\n') * %s''' % (lineCount,),
                number=10000)
            print("\n%9s: %s %s" % (lineCount, a, b))
            self.assertGreater(a, b)