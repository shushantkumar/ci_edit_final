from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timeit import timeit
import unittest

import app.parser


class pt17(unittest.TestCase):
    def test17(self):
       
        if 1:
            # This tests a performance assumption. If this test fails, the
            # program should still work fine, but it may not run as fast as it
            # could by using different assumptions.
            for lineCount in (1,2):
                a = timeit(
                    r'''
foo = pow(foo,3)
''',
                    setup=r'''
foo = 1
''',
                    number=10000)

                b = timeit(
                    r'''
for i in range(0,3):
    foo = foo*foo
''',
                    setup=r'''
foo = 1
''',
                    number=10000)
                print("\n%9s: %s %s" % (lineCount, a, b))