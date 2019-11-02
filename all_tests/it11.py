from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import sys

from app.curses_util import *
import app.fake_curses_testing


class it11(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testit11(self):
        self.runWithFakeInputs([
            self.displayCheck(-1, 0, [u"      "]),
            CTRL_F,
            self.displayCheck(-3, 0, [u"Find: "]),
            CTRL_J,
            self.displayCheck(-1, 0, [u"      "]),
            CTRL_F,
            self.displayCheck(-3, 0, [u"Find: "]),
            CTRL_I,
            self.displayCheck(-3, 0, [u"Find: ", u"Replace: ", u"["]),
            #KEY_BTAB, KEY_BTAB, self.displayCheck(-1, 0, [u"Find: "]),
            CTRL_Q
        ])