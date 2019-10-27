from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import os
import sys

from app.curses_util import *
import app.ci_program
import app.fake_curses_testing
CTRL_C = b'^C'
kTestFile = u'#application_test_file_with_unlikely_file_name~'


class ut1(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def ut1(self):
        self.runWithFakeInputs([
        		self.displayCheck(2, 7, [u"      "]),
            	self.writeText(u"tex"),
            	self.displayCheck(2, 7, [u"tex "]),
            	self.cursorCheck(2, 7),
            	CTRL_C,
                CTRL_Q,
                u'n'
            ])

    def test_write_text(self):
        self.runWithFakeInputs([
            self.writeText(u'test\n'),
            CTRL_Q, u'n'
        ])
