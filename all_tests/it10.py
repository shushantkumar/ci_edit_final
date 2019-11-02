from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest

from app.curses_util import *
import app.fake_curses_testing

class it10(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def test10(self):
        #self.setMovieMode(True)
        lineLimitIndicator = self.prg.prefs.editor['lineLimitIndicator']
        self.prg.prefs.editor['lineLimitIndicator'] = 10
        self.runWithFakeInputs([
            self.displayCheck(2, 7, [u"      "]),
            self.writeText(u"A line with numbers 1234567890"),
            self.displayCheck(2, 7, [u"A line with numbers 1234567890"]),
            self.writeText(u". Writing"),
            self.displayCheck(2, 7, [u"ith numbers 1234567890. Writing"]),
            self.writeText(u" some more."),
            self.displayCheck(2, 7, [u" 1234567890. Writing some more."]),
            self.writeText(u"\n"),
            self.displayCheck(2, 7, [u"A line with numbers 1234567890."]),
            CTRL_Q, u"n"
        ])
        self.prg.prefs.editor['lineLimitIndicator'] = lineLimitIndicator