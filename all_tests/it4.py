from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import os
import sys

from app.curses_util import *
import app.ci_program
import app.fake_curses_testing

kTestFile = u'#startup_test_file_with_unlikely_file_name~'


class it4(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def testit4(self):
        #self.setMovieMode(True)
        self.runWithFakeInputs([
            self.displayCheck(2, 7, [u"// Copyright "]),
            self.cursorCheck(2, 7),
            CTRL_Q
        ], [sys.argv[0], self.pathToSample(u"sample.cc")])