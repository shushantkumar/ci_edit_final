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


class ut37(all_tests.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        all_tests.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testut37(self):
        self.runWithFakeInputs([
            self.displayCheck(0, 0, [
                u" ci     .                               ",
                u"                                        ",
                u"     1                                  ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"New buffer         |    1, 1 |   0%,  0%",
                u"                                        "
            ]),
            self.writeText(u"short line"),
            CTRL_J,
            self.writeText(u"super long line that should go past the screen"),
            CTRL_J,
            self.writeText(u"line that slightly goes off screen"),
            CTRL_J,
            self.writeText(u"short line"),
            CTRL_J,
            self.writeText(u"medium-short line"),
            CTRL_J,
            self.writeText(u"medium-long line that can fit"),
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1 short line                       ",
                u"     2 super long line that should go p ",
                u"     3 line that slightly goes off scre ",
                u"     4 short line                       ",
                u"     5 medium-short line                ",
                u"     6 medium-long line that can fit    ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        6,30 |  83%,100%",
                u"                                        "
            ]),
            KEY_UP,  # Goes to end of 5th line.
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1 short line                       ",
                u"     2 super long line that should go p ",
                u"     3 line that slightly goes off scre ",
                u"     4 short line                       ",
                u"     5 medium-short line                ",
                u"     6 medium-long line that can fit    ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        5,18 |  66%,100%",
                u"                                        "
            ]),
            KEY_UP,  # Goes to end of 4th line.
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1 short line                       ",
                u"     2 super long line that should go p ",
                u"     3 line that slightly goes off scre ",
                u"     4 short line                       ",
                u"     5 medium-short line                ",
                u"     6 medium-long line that can fit    ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        4,11 |  50%,100%",
                u"                                        "
            ]),
            # Should go to column 30 of line 3 since we started at column
            # 30.
            KEY_UP,
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1 short line                       ",
                u"     2 super long line that should go p ",
                u"     3 line that slightly goes off scre ",
                u"     4 short line                       ",
                u"     5 medium-short line                ",
                u"     6 medium-long line that can fit    ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        3,30 |  33%, 85%",
                u"                                        "
            ]),
            KEY_UP,  # Goes to column 30 of line 2.
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1 short line                       ",
                u"     2 super long line that should go p ",
                u"     3 line that slightly goes off scre ",
                u"     4 short line                       ",
                u"     5 medium-short line                ",
                u"     6 medium-long line that can fit    ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        2,30 |  16%, 63%",
                u"                                        "
            ]),
            KEY_UP,  # Goes to end of line 1.
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1 short line                       ",
                u"     2 super long line that should go p ",
                u"     3 line that slightly goes off scre ",
                u"     4 short line                       ",
                u"     5 medium-short line                ",
                u"     6 medium-long line that can fit    ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        1,11 |   0%,100%",
                u"                                        "
            ]),
            # All subsequent KEY_DOWNs should mirror the previous displays.
            KEY_DOWN,
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1 short line                       ",
                u"     2 super long line that should go p ",
                u"     3 line that slightly goes off scre ",
                u"     4 short line                       ",
                u"     5 medium-short line                ",
                u"     6 medium-long line that can fit    ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        2,30 |  16%, 63%",
                u"                                        "
            ]),
            KEY_DOWN,
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1 short line                       ",
                u"     2 super long line that should go p ",
                u"     3 line that slightly goes off scre ",
                u"     4 short line                       ",
                u"     5 medium-short line                ",
                u"     6 medium-long line that can fit    ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        3,30 |  33%, 85%",
                u"                                        "
            ]),
            KEY_DOWN,
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1 short line                       ",
                u"     2 super long line that should go p ",
                u"     3 line that slightly goes off scre ",
                u"     4 short line                       ",
                u"     5 medium-short line                ",
                u"     6 medium-long line that can fit    ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        4,11 |  50%,100%",
                u"                                        "
            ]),
            KEY_DOWN,
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1 short line                       ",
                u"     2 super long line that should go p ",
                u"     3 line that slightly goes off scre ",
                u"     4 short line                       ",
                u"     5 medium-short line                ",
                u"     6 medium-long line that can fit    ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        5,18 |  66%,100%",
                u"                                        "
            ]),
            KEY_DOWN,
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1 short line                       ",
                u"     2 super long line that should go p ",
                u"     3 line that slightly goes off scre ",
                u"     4 short line                       ",
                u"     5 medium-short line                ",
                u"     6 medium-long line that can fit    ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        6,30 |  83%,100%",
                u"                                        "
            ]),
            CTRL_Q, u"n"
            ])

    def test_write_text(self):
        self.runWithFakeInputs([
            self.writeText(u'test\n'),
            CTRL_Q, u'n'
        ])



        