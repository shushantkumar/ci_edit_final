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

class it6(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testit6(self):
        #self.setMovieMode(True)    
        self.assertFalse(os.path.isfile(kTestFile))
        self.runWithFakeInputs([
            self.displayCheck(0, 0, [
                u" ci     .                               ",
            ]),
            u'x',
            CTRL_Q,
            u'y',
            self.writeText(kTestFile),
            CTRL_J,
            CTRL_Q,
        ])
        self.assertTrue(os.path.isfile(kTestFile))
        os.unlink(kTestFile)
        self.assertFalse(os.path.isfile(kTestFile))