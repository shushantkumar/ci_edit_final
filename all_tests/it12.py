from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import sys

from app.curses_util import *
import app.fake_curses_testing


class it12(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)
    def testit12(self):
        self.runWithFakeInputs([
            self.writeText(u"ten one two three\nfour one one five\n"
                           u" six seven one\none\n"),
            self.displayCheck(2, 7, [u"ten one two three  "]),
            self.displayCheck(-1, 0, [u"      "]), CTRL_F,
            self.displayCheck(-3, 0, [u"Find: "]),
            self.writeText(u'one'),
            self.selectionDocumentCheck(0, 4, 0, 7, 3), CTRL_F,
            self.selectionDocumentCheck(1, 5, 1, 8, 3), CTRL_F,
            self.selectionDocumentCheck(1, 9, 1, 12, 3), CTRL_R,
            self.selectionDocumentCheck(1, 5, 1, 8, 3), CTRL_R,
            self.selectionDocumentCheck(0, 4, 0, 7, 3), CTRL_R,
            self.selectionDocumentCheck(3, 0, 3, 3, 3), CTRL_R,
            self.selectionDocumentCheck(2, 11, 2, 14, 3), CTRL_R,
            self.selectionDocumentCheck(1, 9, 1, 12, 3), CTRL_R,
            self.selectionDocumentCheck(1, 5, 1, 8, 3), CTRL_Q, u"n"
        ])