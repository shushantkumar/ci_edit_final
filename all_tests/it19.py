from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import sys

from app.curses_util import *
import app.fake_curses_testing


class it19(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)
    def testit19(self):
        #self.setMovieMode(True)
        self.runWithFakeInputs([
            self.displayCheck(0, 0, [u" ci     "]),
            CTRL_O,
            self.displayCheck(0, 0, [u" ci    Open"]),
            KEY_PAGE_DOWN,
            self.displayFindCheck(u"CONTRIBUTING", u""),
            CTRL_Q,
            # quiting from file manager using two frame updates. 
            CTRL_Q,
        ])