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


class ut34(all_tests.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        all_tests.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testut34(self):
        self.runWithFakeInputs([
            self.writeText(u"carrot\nbanana\nbanana\napple\n"),
            self.displayCheck(2, 7, [
                u"carrot  ", u"banana  ", u"banana  ", u"apple  ",
                u"           "
            ]), CTRL_A, CTRL_E,
            self.writeText(u'|sort'),
            self.displayCheck(-1, 0, [u"e: |sort  "]), CTRL_J,
            self.displayCheck(2, 7, [
                u"apple  ", u"banana  ", u"banana  ", u"carrot  ",
                u"           "
            ]), 
            CTRL_Q, u"n"
            ])

    def test_write_text(self):
        self.runWithFakeInputs([
            self.writeText(u'test\n'),
            CTRL_Q, u'n'
        ])



        