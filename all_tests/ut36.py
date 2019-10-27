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


class ut36(all_tests.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        all_tests.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testut36(self):
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
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1 rt line                          ",
                u"     2 er long line that should go past ",
                u"     3 e that slightly goes off screen  ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        3,35 |  66%,100%",
                u"                                        "
            ]),
            KEY_UP,
            KEY_END,  # Place cursor at the end of the second line.
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1                                  ",
                u"     2  that should go past the screen  ",
                u"     3 tly goes off screen              ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        2,47 |  33%,100%",
                u"                                        "
            ]),
            # scrollCol should be set to 0 since line 1 fits on screen.
            KEY_UP,
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1 short line                       ",
                u"     2 super long line that should go p ",
                u"     3 line that slightly goes off scre ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        1,11 |   0%,100%",
                u"                                        "
            ]),
            # cursor should snap back to the end of the second line.
            KEY_DOWN,
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1                                  ",
                u"     2  that should go past the screen  ",
                u"     3 tly goes off screen              ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        2,47 |  33%,100%",
                u"                                        "
            ]),
            # scrollCol should not change since line 1 doesn't fit on
            # screen.
            KEY_DOWN,
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1                                  ",
                u"     2  that should go past the screen  ",
                u"     3 tly goes off screen              ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        3,35 |  66%,100%",
                u"                                        "
            ]),
            KEY_UP,  # cursor moves back to original position.
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1                                  ",
                u"     2  that should go past the screen  ",
                u"     3 tly goes off screen              ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        2,47 |  33%,100%",
                u"                                        "
            ]),
            # Make line 3 fit on screen. This includes making room for the
            # cursor.
            KEY_DOWN,
            KEY_BACKSPACE1,
            KEY_BACKSPACE1,
            KEY_BACKSPACE1,
            KEY_UP,
            # Since line 3 now fits on screen, this should set scrollCol to
            # 0.
            KEY_DOWN,
            self.displayCheck(0, 0, [
                u" ci     *                               ",
                u"                                        ",
                u"     1 short line                       ",
                u"     2 super long line that should go p ",
                u"     3 line that slightly goes off scr  ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                                        ",
                u"                        3,32 |  66%,100%",
                u"                                        "
            ]),
            CTRL_Q, u"n"
            ])

    def test_write_text(self):
        self.runWithFakeInputs([
            self.writeText(u'test\n'),
            CTRL_Q, u'n'
        ])



        