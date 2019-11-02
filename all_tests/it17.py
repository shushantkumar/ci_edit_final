from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import sys

from app.curses_util import *
import app.fake_curses_testing


class it17(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)
    def testit17(self):
        #self.setMovieMode(True)
        self.runWithFakeInputs([
            self.displayCheck(0, 0, [u" ci     "]),
            self.displayCheck(2, 7, [u"     "]), CTRL_S,
            self.displayCheck(0, 0, [u" ci    Save File As"]), CTRL_Q, CTRL_Q
        ])  