from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timeit import timeit
import unittest

import app.parser


class pt20(unittest.TestCase):
    def test20(self):
       
        if 1:
            # This tests a performance assumption. If this test fails, the
            # program should still work fine, but it may not run as fast as it
            # could by using different assumptions.
            for lineCount in (1,2):
                a = timeit(
                    r'''
total = sum(foo)
''',
                    setup=r'''
import random
foo = []
for i in range(0,100):
    foo.append(random.randint(1,101))
''',
                    number=10000)

                b = timeit(
                    r'''
total = 0
for i in range(0,100):
    total+=foo[i]
''',
                    setup=r'''
import random
foo = []
for i in range(0,100):
    foo.append(random.randint(1,101))
''',
                    number=10000)
                print("\n%9s: %s %s" % (lineCount, a, b))