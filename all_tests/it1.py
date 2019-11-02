from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import os
import sys

from app.curses_util import *
import app.ci_program
import app.fake_curses_testing

kTestFile = u'#application_test_file_with_unlikely_file_name~'


class it1(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testit1(self):
        self.runWithFakeInputs([
                self.displayCheck(2, 7, [u"      "]),
                curses.ascii.ESC,
                app.curses_util.BRACKETED_PASTE_BEGIN,
                u't',
                u'e',
                225,
                186,
                191,  # Send an "" in utf-8.
                u't',
                curses.ascii.ESC,
                app.curses_util.BRACKETED_PASTE_END,
                self.displayCheck(2, 7, [u'te\u1ebft ']),
                CTRL_Q,
                u'n'
            ])

    def test_write_text(self):
        self.runWithFakeInputs([
            self.writeText(u'test\n'),
            CTRL_Q, u'n'
        ])
