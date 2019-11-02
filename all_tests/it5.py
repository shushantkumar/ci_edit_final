from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import os
import sys

from app.curses_util import *
import app.ci_program
import app.fake_curses_testing

kTestFile = u'#application_test_file_with_unlikely_file_name~'

class it5(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testit5(self):
        #self.setMovieMode(True)
        self.runWithFakeInputs([
            self.displayCheck(0, 0, [
                u" ci     .                               ",
            ]), u'x', CTRL_Q, u'c',
            self.writeText(u' after cancel'),
            self.displayCheck(2, 7, [
                u"x after cancel ",
            ]), CTRL_Q, u'n'
        ])

    