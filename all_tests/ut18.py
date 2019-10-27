from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import os
import sys

from all_tests.curses_util import *
import all_tests.ci_program
import all_tests.fake_curses_testing
# CTRL_X = b'^X'
kTestFile = u'#all_testslication_test_file_with_unlikely_file_name~'


class ut18(all_tests.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        all_tests.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testut18(self):
        self.runWithFakeInputs([
            self.displayCheck(2, 7, [u"      "]),
            self.writeText(u"one two "),
            self.displayCheck(2, 7, [u"one two "]),
            self.writeText(u"three four "),
            self.displayCheck(2, 7, [u"one two three four", "     "]),
            KEY_SHIFT_LEFT, KEY_SHIFT_LEFT, KEY_SHIFT_LEFT, KEY_SHIFT_LEFT,
            KEY_SHIFT_LEFT, KEY_SHIFT_LEFT, KEY_SHIFT_LEFT, KEY_SHIFT_LEFT,
            KEY_SHIFT_LEFT, KEY_SHIFT_LEFT, KEY_SHIFT_LEFT, KEY_SHIFT_LEFT,
            KEY_SHIFT_LEFT, KEY_SHIFT_LEFT, KEY_SHIFT_LEFT,
            self.writeText(u"five "),
            self.displayCheck(2, 7, [u"one five"]), CTRL_Z,
            self.displayCheck(2, 7, [u"one two three four        "]), CTRL_Z,
            self.displayCheck(2, 7, [u"one two        "]), CTRL_Y,
            self.displayCheck(2, 7, [u"one two three four        "]), CTRL_Y,
            self.displayCheck(2, 7, [u"one five        "]), CTRL_Q, u"n"
            ])

    def test_write_text(self):
        self.runWithFakeInputs([
            self.writeText(u'test\n'),
            CTRL_Q, u'n'
        ])
