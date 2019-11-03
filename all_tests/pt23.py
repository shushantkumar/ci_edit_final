from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timeit import timeit
import unittest

import app.parser


class pt23(unittest.TestCase):
    def test23(self):
       
        if 1:
            # This tests a performance assumption. If this test fails, the
            # program should still work fine, but it may not run as fast as it
            # could by using different assumptions.
            for lineCount in (1,2):
                a = timeit(
                    r'''
final = str.count(text,'a')
''',
                    setup=r'''
text = 'a'*10000
''',
                    number=100)

                b = timeit(
                    r'''
sum=0
for i in range(0,10000):
    if (text[i]=='a'):
        sum+=1
''',
                    setup=r'''
text = 'a'*10000
''',
                    number=100)
                print("\n%9s: %s %s" % (lineCount, a, b))