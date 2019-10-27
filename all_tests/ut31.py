from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import os
import sys

from all_tests.curses_util import *
import all_tests.ci_program
import all_tests.fake_curses_testing

kTestFile = u'#all_testslication_test_file_with_unlikely_file_name~'


class ut31(all_tests.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        all_tests.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testut31(self):
        self.runWithFakeInputs([
            self.cursorCheck(2, 7),
            self.writeText(u'test\napple\norange\none\ntwenty five'),
            self.cursorCheck(6, 18),
            self.displayCheck(-2, 0, [u"             ",]),            
            self.addMouseInfo(0, 2, 10, curses.BUTTON1_PRESSED),
            curses.KEY_MOUSE,
            self.displayCheck(-2, 0, [u"9 characters (4 lines) selected",]),
            self.selectionCheck(4, 11, 0, 3, 2),
            CTRL_Q, u"n"
            ])

    def test_write_text(self):
        self.runWithFakeInputs([
            self.writeText(u'test\n'),
            CTRL_Q, u'n'
        ])