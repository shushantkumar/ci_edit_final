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


class ut17(all_tests.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        all_tests.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testut17(self):
        lineLimitIndicator = self.prg.prefs.editor['lineLimitIndicator']
        self.prg.prefs.editor['lineLimitIndicator'] = 10
        self.runWithFakeInputs([
            self.displayCheck(2, 7, [u"      "]),
            self.writeText(u"A line with numbers 1234567890"),
            self.displayCheck(2, 7, [u"A line with numbers 1234567890"]),
            self.writeText(u". Writing"),
            self.displayCheck(2, 7, [u"ith numbers 1234567890. Writing"]),
            self.writeText(u" some more."),
            self.displayCheck(2, 7, [u" 1234567890. Writing some more."]),
            self.writeText(u"\n"),
            self.displayCheck(2, 7, [u"A line with numbers 1234567890."]),
            CTRL_Q, u"n"
        ])
        self.prg.prefs.editor['lineLimitIndicator'] = lineLimitIndicator

    def test_write_text(self):
        self.runWithFakeInputs([
            self.writeText(u'test\n'),
            CTRL_Q, u'n'
        ])
