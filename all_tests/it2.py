from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import sys

from app.curses_util import *
import app.fake_curses_testing


class it2(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)
    def testit2(self):
        self.runWithFakeInputs([
            self.displayCheck(2, 7, [u"     "]),
            self.writeText(u'text'), 
            self.displayCheck(2, 7, [u"text "]),CTRL_A, CTRL_C, KEY_LEFT, CTRL_V,
            self.displayCheck(2, 7, [u"text"]), CTRL_Q, u"n"
        ])