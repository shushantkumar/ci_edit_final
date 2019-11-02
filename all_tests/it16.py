from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import sys

from app.curses_util import *
import app.fake_curses_testing


class it16(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)
    def testit16(self):
        self.runWithFakeInputs([
            #self.displayCheck(2, 7, [u"      "]),
            #self.displayCheckStyle(2, 7, 1, 10,
            #    self.prg.color.get(u'text', 0)),
            self.writeText(u'focusedWindow\n'),
            CTRL_F,
            #self.displayCheck(-1, 0, [u"Find:         "]),
            self.writeText(u'focused'),
            CTRL_I,
            #self.displayCheck(
            #    -3, 0, [u"Find: focused", "Replace:          ", u"["]),
            self.writeText(u'  focused'),
            #self.displayCheck(
            #    -3, 0, [u"Find: focused", "Replace:   focused", u"["]),
            CTRL_G,
            # Regression, replace causes 'Windo' to show as a misspelling.
            self.displayCheckStyle(2, 17, 1, 10, self.prg.color.get(u'text',
                                                                    0)),
            CTRL_Q,
            ord('n')
        ])