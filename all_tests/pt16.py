from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timeit import timeit
import unittest

import app.parser


class pt16(unittest.TestCase):
    def test16(self):
       
        if 1:
            # This tests a performance assumption. If this test fails, the
            # program should still work fine, but it may not run as fast as it
            # could by using different assumptions.
            for lineCount in (100, 1000, 100000):
                a = timeit(
                    r'''
foo = abs(foo)
''',
                    setup=r'''
foo = -1
''',
                    number=10000)

                b = timeit(
                    r'''
if (-foo>=0):
    foo = -1
else:
    pass
''',
                    setup=r'''
foo = -1
''',
                    number=10000)
                print("\n%9s: %s %s" % (lineCount, a, b))