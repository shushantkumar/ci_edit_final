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


class ut16(all_tests.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        all_tests.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testut16(self):
        self.runWithFakeInputs([
            self.displayCheck(2, 7, [u"      "]),
            self.writeText(u"tex"),
            self.displayCheck(2, 7, [u"tex "]), KEY_BACKSPACE1, u"t",
            self.displayCheck(2, 7, [u"tet "]), CTRL_Q, u"n"
        ])

    def testut_16(self):
        test = u"""\t<tab
\t <tab+space
 \t<space+tab
\ta<
a\t<
some text.>\t<
\t\t<2tabs
line\twith\ttabs
ends with tab>\t
\t
"""
        self.runWithFakeInputs([
            self.displayCheck(2, 7, [u"                           "]),
            self.writeText(test),
            self.displayCheck(2, 7, [u"        <tab               "]),
            self.displayCheck(3, 7, [u"         <tab+space        "]),
            self.displayCheck(4, 7, [u"        <space+tab         "]),
            self.displayCheck(5, 7, [u"        a<                 "]),
            self.displayCheck(6, 7, [u"a       <                  "]),
            self.displayCheck(7, 7, [u"some text.>     <          "]),
            self.displayCheck(8, 7, [u"                <2tabs     "]),
            self.displayCheck(9, 7, [u"line    with    tabs       "]),
            self.displayCheck(10, 7, [u"ends with tab>             "]),
            self.displayCheck(11, 7, [u"                           "]),
            CTRL_Q, u"n"
        ])

