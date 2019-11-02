from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import sys

from app.curses_util import *
import app.fake_curses_testing


class it18(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)
    def testit18(self):
        """Avoid crash when pressing return when the path input is empty."""
        #self.setMovieMode(True)
        self.runWithFakeInputs([
            self.displayCheck(0, 0, [u" ci     "]),
            self.displayCheck(2, 7, [u"     "]),
            CTRL_O,
            self.displayCheck(0, 0, [u" ci    Open File  "]),
            CTRL_A,
            KEY_BACKSPACE1,
            self.displayCheck(2, 7, [u"     "]),
            CTRL_J,
            self.displayCheck(0, 0, [u" ci    Open File  "]),
            KEY_ESCAPE,
            curses.ERR,
            self.displayCheck(0, 0, [u" ci     "]),
            CTRL_Q,
        ]) 