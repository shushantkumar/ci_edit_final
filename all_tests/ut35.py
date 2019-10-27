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


class ut35(all_tests.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        all_tests.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testut35(self):
        self.runWithFakeInputs([
            self.displayCheck(0, 0, [u" ci  "]),
            self.cursorCheck(2, 7),
            self.writeText(u'test asdf orange'),
            self.selectionCheck(0, 16, 0, 0, 0),
            self.displayCheckStyle(2, 7, 1, len(u"test "),
                                   self.prg.color.get(u'text', 0)),
            self.displayCheckStyle(2, 12, 1, len(u"asdf"),
                                   self.prg.color.get(u'misspelling', 0)),
            self.displayCheckStyle(2, 16, 1, len(u" orange"),
                                   self.prg.color.get(u'text', 0)),
            CTRL_Q, u"n"
            ])

    def test_write_text(self):
        self.runWithFakeInputs([
            self.writeText(u'test\n'),
            CTRL_Q, u'n'
        ])



        