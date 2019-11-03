from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timeit import timeit
import unittest, time

import app.parser


class pt21(unittest.TestCase):
    def test21(self):
       
        if 1:
            # This tests a performance assumption. If this test fails, the
            # program should still work fine, but it may not run as fast as it
            # could by using different assumptions.
            for lineCount in (1,2):
                a = timeit(
                    r'''
total = sum(foo[0][0], 0)
''',
                    setup=r'''
import random
foo = [[[0 for k in range(100)] for j in range(10)] for i in range(10)]
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,100):
            foo[i][j][k] = random.randint(1,10) 
''',
                    number=10000)

                b = timeit(
                    r'''
total = 0
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,100):
            total= total+foo[i][j][k]
''',
                    setup=r'''
import random
foo = [[[0 for k in range(100)] for j in range(10)] for i in range(10)]
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,100):
            foo[i][j][k] = random.randint(1,101)
''',
                    number=10000)
                print("\n%9s: %s %s" % (lineCount,a,  b))