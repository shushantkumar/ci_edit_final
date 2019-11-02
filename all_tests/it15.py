from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import sys

from app.curses_util import *
import app.fake_curses_testing


class it15(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)
    def testit15(self):
        self.runWithFakeInputs([
            # Check initial state.
            self.displayCheck(-1, 0, [u"      "]),
            self.displayCheckStyle(-2, 0, 1, 10,
                                   self.prg.color.get(u'status_line', 0)),

            # Basic open and close.
            CTRL_F,
            self.displayCheck(-3, 0, [u"Find: "]),
            KEY_ESCAPE,
            curses.ERR,
            self.displayCheck(-3, 0, [u"   ", u"   ", u"   "]),
            self.displayCheckStyle(-2, 0, 1, 10,
                                   self.prg.color.get(u'status_line', 0)),
            # Quit without saving.
            CTRL_Q
        ])