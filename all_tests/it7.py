from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest

from app.curses_util import *
import app.fake_curses_testing


class it7(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testit7(self):
        self.runWithFakeInputs([
            self.displayCheck(2, 7, [u"      "]),
            self.writeText(u"abcdefghij"),
            self.displayCheck(2, 7, [u"abcdefghij "]), CTRL_A,
            self.writeText(u"x"),
            self.displayCheck(2, 7, [u"x "]), CTRL_Q, u"n"
        ])