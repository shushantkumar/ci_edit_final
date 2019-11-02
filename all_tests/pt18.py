from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timeit import timeit
import unittest

import app.parser


class pt18(unittest.TestCase):
    def test18(self):
       
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
foo = power(1,3)
''',
                    setup=r'''
foo = 1
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return (base*power(base,exp-1))
''',
                    number=10000)
                print("\n%9s: %s %s" % (lineCount, a, b))