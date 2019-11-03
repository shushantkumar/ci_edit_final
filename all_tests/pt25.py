from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timeit import timeit
import unittest

import app.parser


class pt25(unittest.TestCase):
    def test25(self):
       
        if 1:
            # This tests a performance assumption. If this test fails, the
            # program should still work fine, but it may not run as fast as it
            # could by using different assumptions.
            for lineCount in (1,2):
                a = timeit(
                    r'''
final = text.index('b')
''',
                    setup=r'''
text = 'a'*10000+'b'*4
''',
                    number=1000)

                b = timeit(
                    r'''
count = 0
for j in text:
    if (j=='b'):
        break
    count+=1

''',
                    setup=r'''
text = 'a'*10000 + 'b'*4
''',
                    number=1000)
                print("\n%9s: %s %s" % (lineCount, a, b))