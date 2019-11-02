from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import sys

from app.curses_util import *
import app.fake_curses_testing


class it14(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)
    def testit14(self):
        #self.setMovieMode(True)
        self.runWithFakeInputs([
            self.writeText(u'a\nb\na\nb\na\nb\n'),
            self.displayCheck(2, 7, [u"a ", u"b ", u"a ", u"b ", u"a ", u"b "]),

            # Enter Find and make two document replacements.
            CTRL_F,
            self.writeText(u'(a)'),
            self.displayCheck(-3, 0, [u"Find: (a)  "]),
            CTRL_I,
            self.writeText(u'\\1!\\1'),
            self.displayCheck(-2, 0, [u"Replace: \\1!\\1  "]),
            CTRL_G,
            self.displayCheck(2, 7,
                              [u"a!a ", u"b ", u"a ", u"b ", u"a ", u"b "]),
            CTRL_G,
            self.displayCheck(2, 7,
                              [u"a!a ", u"b ", u"a!a ", u"b ", u"a ", u"b "]),
            
            CTRL_G,
            self.displayCheck(2, 7,
                              [u"a!a ", u"b ", u"a!a ", u"b ", u"a!a ", u"b "]),

            
            # Quit without saving.
            CTRL_Q,
            u"n"
        ])