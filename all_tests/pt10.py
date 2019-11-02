from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timeit import timeit
import unittest

import app.parser


class pt10(unittest.TestCase):
    def testpt10(self):
        # This tests a performance assumption. If this test fails, the
        # program should still work fine, but it may not run as fast as it
        # could by using different assumptions.
        #
        # Insert into an array of strings is expected to be faster than
        # insert into a contiguous buffer of similar size.
        #
        # This is why ci_edit uses both a self.data buffer and a
        # self.lines[] array. Though splitting the data into lines is also
        # expensive, see tests below.
        #
        # At 1,000 bytes the performance is similar.
        a = timeit(
            'data1 = data1[:500] + "x" + data1[500:]',
            setup='data1 = "a" * 1000',
            number=10000)
        b = timeit(
            'data2[5] = data2[5][:50] + "x" + data2[5][50:]',
            setup='data2 = ["a" * 100] * 10',
            number=10000)
        self.assertGreater(a, b * 0.8)
        self.assertLess(a, b * 4)
        # At 10,000 bytes the array of strings is 1.4 to 3 times faster.
        a = timeit(
            'data1 = data1[:5000] + "x" + data1[5000:]',
            setup='data1 = "a" * 10000',
            number=10000)
        b = timeit(
            'data2[50] = data2[50][:50] + "x" + data2[50][50:]',
            setup='data2 = ["a" * 100] * 100',
            number=10000)
        self.assertGreater(a, b * 1.4)
        self.assertLess(a, b * 4)
        # At 100,000 bytes the array of strings is 12 to 24 times faster.
        a = timeit(
            'data1 = data1[:50000] + "x" + data1[50000:]',
            setup='data1 = "a" * 100000',
            number=10000)
        b = timeit(
            'data2[500] = data2[500][:50] + "x" + data2[500][50:]',
            setup='data2 = ["a" * 100] * 1000',
            number=10000)
        self.assertGreater(a, b * 8)
        self.assertLess(a, b * 24)