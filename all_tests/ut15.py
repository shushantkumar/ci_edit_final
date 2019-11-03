from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import os
import sys

from all_tests.curses_util import *
import all_tests.ci_program
import all_tests.fake_curses_testing
import all_tests.line_buffer

kTestFile = u'#all_testslication_test_file_with_unlikely_file_name~'


class ut15(all_tests.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        all_tests.fake_curses_testing.FakeCursesTestCase.setUp(self)
        self.line_buffer = app.line_buffer.LineBuffer(app.ci_program.CiProgram())
        app.log.shouldWritePrintLog = True

    def testut15(self):
        self.runWithFakeInputs([
            self.assertTrue(self.line_buffer is not None),
            self.displayCheck(2, 7, [u"      "]),
            self.cursorCheck(2, 7),
            self.writeText(u'test\napple\norange'),
            self.cursorCheck(4, 13),
            self.selectionCheck(2, 6, 0, 0, 0), KEY_UP,
            self.cursorCheck(3, 12),
            self.selectionCheck(1, 5, 0, 0, 0), KEY_SHIFT_LEFT,
            self.cursorCheck(3, 11),
            self.selectionCheck(1, 4, 1, 5, 3), KEY_SHIFT_RIGHT,
            self.cursorCheck(3, 12),
            CTRL_Q, u"n"
            ])

    def test_write_text(self):
        self.runWithFakeInputs([
            self.writeText(u'test\n'),
            CTRL_Q, u'n'
        ])
