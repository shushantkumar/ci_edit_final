from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import os
import sys
import unittest
from all_tests.curses_util import *
import all_tests.ci_program
import all_tests.fake_curses_testing

kTestFile = u'#all_testslication_test_file_with_unlikely_file_name~'


class ut39(all_tests.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        all_tests.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testut39(self):
        def testNumber(strInput, reg):
            sre = app.regex.kReNumbers.search(strInput)
            if sre is None:
                self.assertEqual(sre, reg)
                return
            self.assertEqual(reg, sre.regs[0])

        testNumber('0342', (0, 4))




        