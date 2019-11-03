from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest

from app.curses_util import *
import app.fake_curses_testing


import os
import app.log
import app.text_buffer


class FakeCursorWindow:
    def getmaxyx(self):
        return (100, 100)

class FakeView:
    def __init__(self):
        self.cursorWindow = FakeCursorWindow()
        self.top = 0
        self.left = 0
        self.rows = 10
        self.cols = 100
        self.scrollRow = 0
        self.scrollCol = 0

class it9(app.fake_curses_testing.FakeCursesTestCase):

    def setUp(self):
        
        # app.log.shouldWritePrintLog = False
        # self.prg = app.ci_program.CiProgram()
        # self.textBuffer = app.text_buffer.TextBuffer(self.prg)
        # self.textBuffer.setView(FakeView())
        app.fake_curses_testing.FakeCursesTestCase.setUp(self)
        self.textBuffer = app.text_buffer.TextBuffer(self.prg)

    def testit9(self):
        self.runWithFakeInputs([
            self.displayCheck(2, 7, [u"      "]),
            self.writeText(u"()"),
            self.displayCheck(2, 7, [u"() "]),
            self.writeText(u"x"),

            self.selectionCheck(0, 3, 0, 0, 0), KEY_SHIFT_LEFT,
            CTRL_X,
            KEY_LEFT,
            
            CTRL_V,
            self.displayCheck(2, 7, [u"(x)"]), 
            CTRL_Q, u"n"
        ])