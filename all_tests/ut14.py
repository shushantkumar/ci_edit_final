from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import unittest

import app.string


class ut14(unittest.TestCase):

    def testut14(self):
        tests = [
            (u"abcd", u"abcd"),
            (u"\rabcd", u"\\rabcd"),
            (u"ab\rcd", u"ab\\rcd"),
            (u"abcd\r", u"abcd\\r"),
            (u"\aab\tcd\r", u"\\aab\\tcd\\r"),
            (u"abcd\\", u"abcd\\\\"),
            (u"\\", u"\\\\"),
        ]
        for test in tests:
            self.assertEqual(app.string.pathDecode(test[1]), test[0])
