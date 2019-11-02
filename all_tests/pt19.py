from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timeit import timeit
import unittest

import app.parser


class pt19(unittest.TestCase):
    def test19(self):
       
        if 1:
            # This tests a performance assumption. If this test fails, the
            # program should still work fine, but it may not run as fast as it
            # could by using different assumptions.
            for lineCount in (1,2):
                a = timeit(
                    r'''
sorted(foo)
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
quickSort(foo,0,99) 
''',
                    setup=r'''
import random
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
foo = []
for i in range(0,100):
    foo.append(random.randint(1,101))
''',
                    number=10000)
                print("\n%9s: %s %s" % (lineCount, a, b))