from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import sys

from app.curses_util import *
import app.fake_curses_testing


class it13(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)
    def testit13(self):
        #self.setMovieMode(True)
        self.runWithFakeInputs([
            self.writeText(u"aClass\n"),
            self.displayCheck(2, 7, [u"aClass  "]), CTRL_F,
            self.writeText(u'a(.*)'),
            self.displayCheck(-3, 0, [u"Find: a(.*)  "]), CTRL_I,
            self.writeText(u'x\\1\\1'),
            self.displayCheck(-2, 0, [u"Replace: x\\1\\1  "]), CTRL_G,
            self.displayCheck(2, 7, [u"xClassClass  "]), CTRL_Q, u"n"
        ])