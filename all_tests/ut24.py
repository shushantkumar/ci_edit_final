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


class ut24(all_tests.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        all_tests.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testut24(self):
        write = self.writeText
        checkStyle = self.displayCheckStyle
        bracketColor = self.prg.color.get(u'bracket', 0)
        defaultColor = self.prg.color.get(u'default', 0)
        matchingBracketColor = self.prg.color.get(u'matching_bracket', 0)
        self.runWithFakeInputs([
            write(u'{test}'),
            self.displayCheck(2, 7, [u"{test}    "]),
            checkStyle(2, 7, 1, 1, bracketColor),
            checkStyle(2, 8, 1, 4, defaultColor),
            checkStyle(2, 12, 1, 1, bracketColor),
            CTRL_Q, u"n"
            ])

    def test_write_text(self):
        self.runWithFakeInputs([
            self.writeText(u'test\n'),
            CTRL_Q, u'n'
        ])