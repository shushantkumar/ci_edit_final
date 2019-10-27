from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import os
import sys

from all_tests.curses_util import *
import all_tests.ci_program
import all_tests.fake_curses_testing
CTRL_X = b'^X'
kTestFile = u'#all_testslication_test_file_with_unlikely_file_name~'


class ut20(all_tests.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        all_tests.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testut20(self):
        self.runWithFakeInputs([
            self.cursorCheck(2, 7),
            self.writeText(u'test\napple\norange'),
            self.cursorCheck(4, 13),
            self.selectionCheck(2, 6, 0, 0, 0),
            KEY_SHIFT_UP,
            self.cursorCheck(3, 12),
            self.selectionCheck(1, 5, 2, 6, 3),
            KEY_SHIFT_UP,
            self.cursorCheck(2, 11),
            self.selectionCheck(0, 4, 2, 6, 3),
            # Regression test: shift down past the end of the document
            # should select to end of document (i.e. end of line).
            KEY_SHIFT_UP,
            self.cursorCheck(2, 7),
            self.selectionCheck(0, 0, 2, 6, 3),
            # Same for non-selection.
            KEY_DOWN,
            KEY_END,
            self.cursorCheck(3, 12),
            self.selectionCheck(1, 5, 0, 0, 0),
            CTRL_Q, u"n"
            ])

    def test_write_text(self):
        self.runWithFakeInputs([
            self.writeText(u'test\n'),
            CTRL_Q, u'n'
        ])