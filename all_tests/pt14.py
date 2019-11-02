from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timeit import timeit
import unittest

import app.parser


class pt14(unittest.TestCase):

    
    def testpt14(self):
        # Disabled due to running time.
        if 1:
            # This tests a performance assumption. If this test fails, the
            # program should still work fine, but it may not run as fast as it
            # could by using different assumptions.
            for lineCount in (100, 1000, 5000):
                a = timeit(
                    r'''
a = Node()
a.foo = 5
a.bar = 'hi'
a.blah = 7
foo.append(a)
''',
                    setup=r'''
foo = []
class Node:
  def __init__(self):
    self.foo = None
    self.bar = None
    self.blah = None
''',
                    number=10000)
                b = timeit(
                    r'''
a = (5, 'hi', 7)
foo = (foo,)+a
''',
                    setup=r'''
foo = []
''',
                    number=10000)
                print("\n%9s: %s %s" % (lineCount, a, b))