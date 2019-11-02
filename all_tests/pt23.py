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
final = str.partition(text,'a')
''',
                    setup=r'''
text = 'a'*10000
''',
                    number=100)

                b = timeit(
                    r'''
divideString('a'*10000,10000)
''',
                    setup=r'''
def divideString(string, n): 
    str_size = len(string) 
  
    # Check if string can be divided in n equal parts 
    if str_size % n != 0: 
        return
  
    # Calculate the size of parts to find the division points 
    part_size = str_size/n 
    k = 0
    for i in string: 
        if k%part_size==0: 
          pass  
        k += 1
''',
                    number=100)
                print("\n%9s: %s %s" % (lineCount, a, b))