from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import os
import sys

from all_tests.curses_util import *
import all_tests.ci_program
import all_tests.fake_curses_testing
CTRL_X = b'^X'
kTestFile = u'#all_testslication_test_file_with_unlikely_file_name~'


class ut2(all_tests.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        self.longMessage = True
        all_tests.fake_curses_testing.FakeCursesTestCase.setUp(self)

    def ut2(self):
        self.runWithFakeInputs([
        		self.displayCheck(2, 7, [u"      "]),
            	self.writeText(u"tex"),
            	self.displayCheck(2, 7, [u"tex "]),
            	self.cursorCheck(2, 7),
            	CTRL_X,
                self.displayCheck(2, 7, [u"      "]),
                CTRL_Q,
                u'n'
            ])

    def test_write_text(self):
        self.runWithFakeInputs([
            self.writeText(u'test\n'),
            CTRL_Q, u'n'
        ])
