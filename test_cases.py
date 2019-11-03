

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
if not os.getenv('CI_EDIT_USE_REAL_CURSES'):
    # Replace curses with a fake version for testing.
    sys.path = [os.path.join(os.path.dirname(__file__), 'test_fake')] + sys.path
    import all_tests.log
    all_tests.log.enabledChannels = {
        'error': True,
        'info': True,
        'meta': True,
        'mouse': True,
        'startup': True
    }
    all_tests.log.shouldWritePrintLog = True

import unittest

# Set up strict_debug before loading other all_tests.* modules.
import all_tests.config
all_tests.config.strict_debug = True

import all_tests.ut1
import all_tests.ut2
import all_tests.ut3
import all_tests.ut4
import all_tests.ut5
import all_tests.ut6
import all_tests.ut7
import all_tests.ut8
import all_tests.ut9
import all_tests.ut10
import all_tests.ut11
import all_tests.ut12
import all_tests.ut13
import all_tests.ut14
import all_tests.ut15
import all_tests.ut16
import all_tests.ut17
import all_tests.ut18
import all_tests.ut19
import all_tests.ut20
import all_tests.ut21
import all_tests.ut22
import all_tests.ut23
import all_tests.ut24
import all_tests.ut25
import all_tests.ut26
import all_tests.ut27
import all_tests.ut28
import all_tests.ut29
import all_tests.ut30
import all_tests.ut31
import all_tests.ut32
import all_tests.ut33
import all_tests.ut34
import all_tests.ut35
import all_tests.ut36
import all_tests.ut37
import all_tests.ut38
import all_tests.ut39
import all_tests.ut40

import all_tests.it1
import all_tests.it2
import all_tests.it3
import all_tests.it4
import all_tests.it5
import all_tests.it6
import all_tests.it7
import all_tests.it8
import all_tests.it9  # dont know how to do
import all_tests.it10
import all_tests.it11
import all_tests.it12
import all_tests.it13
import all_tests.it14
import all_tests.it15
import all_tests.it16
import all_tests.it17
import all_tests.it18
import all_tests.it19  # test case failed
import all_tests.it20

import all_tests.pt1
import all_tests.pt2
import all_tests.pt3
import all_tests.pt4
import all_tests.pt5
import all_tests.pt6
import all_tests.pt7
import all_tests.pt8
import all_tests.pt10
import all_tests.pt11
import all_tests.pt12
import all_tests.pt13
import all_tests.pt14
import all_tests.pt15
import all_tests.pt16
import all_tests.pt17
import all_tests.pt18
import all_tests.pt19
import all_tests.pt20
import all_tests.pt21 # not working
import all_tests.pt22
import all_tests.pt23
import all_tests.pt24
import all_tests.pt25
# import all_tests.unit_test_actions
# import all_tests.unit_test_application
# import all_tests.unit_test_automatic_column_adjustment
# import all_tests.unit_test_bookmarks
# import all_tests.unit_test_brace_matching
# import all_tests.unit_test_buffer_file
# import all_tests.unit_test_copy_paste
# import all_tests.unit_test_curses_util
# import all_tests.unit_test_execute_prompt
# import all_tests.unit_test_file_manager
# import all_tests.unit_test_find_window
# import all_tests.unit_test_intention
# import all_tests.unit_test_line_buffer
# import all_tests.unit_test_misspellings
# import all_tests.unit_test_parser
# import all_tests.unit_test_performance
# import all_tests.unit_test_prediction_window
# import all_tests.unit_test_prefs
# import all_tests.unit_test_regex
# import all_tests.unit_test_selectable
# import all_tests.unit_test_startup
# import all_tests.unit_test_string
# import all_tests.unit_test_text_buffer
# import all_tests.unit_test_ui
# import all_tests.unit_test_undo_redo

# Add new test cases here.
TESTS = {
	'ut1':
	all_tests.ut1.ut1,
	'ut2':
	all_tests.ut2.ut2,
	'ut3':
	all_tests.ut3.ut3,
	'ut4':
	all_tests.ut4.ut4,
	'ut5':
	all_tests.ut5.ut5,
	'ut6':
	all_tests.ut6.ut6,
	'ut7':
	all_tests.ut7.ut7,
	'ut8':
	all_tests.ut8.ut8,
	'ut9':
	all_tests.ut9.ut9,
	'ut10':
	all_tests.ut10.ut10,
	'ut11':
	all_tests.ut11.ut11,
	'ut12':
	all_tests.ut12.ut12,
	'ut13':
	all_tests.ut13.ut13,
	'ut14':
	all_tests.ut14.ut14,
	# 'ut15':
	# all_tests.ut15.ut15,
	# 'ut16':
	# all_tests.ut16.ut16,
	# 'ut17':
	# all_tests.ut17.ut17,
	'ut18':
	all_tests.ut18.ut18,
	'ut19':
	all_tests.ut19.ut19,
	'ut20':
	all_tests.ut20.ut20,
	'ut21':
	all_tests.ut21.ut21,
	'ut22':
	all_tests.ut22.ut22,
	'ut23':
	all_tests.ut23.ut23,
	'ut24':
	all_tests.ut24.ut24,
	'ut25':
	all_tests.ut25.ut25,
	'ut26':
	all_tests.ut26.ut26,
	'ut27':
	all_tests.ut27.ut27,
	'ut28':
	all_tests.ut28.ut28,
	'ut29':
	all_tests.ut29.ut29,
	'ut30':
	all_tests.ut30.ut30,
	'ut31':
	all_tests.ut31.ut31,
	'ut32':
	all_tests.ut32.ut32,
	'ut33':
	all_tests.ut33.ut33,
	'ut34':
	all_tests.ut34.ut34,
	'ut35':
	all_tests.ut35.ut35,
	'ut36':
	all_tests.ut36.ut36,
	'ut37':
	all_tests.ut37.ut37,
	'ut38':
	all_tests.ut38.ut38,
	'ut39':
	all_tests.ut39.ut39,
	'ut40':
	all_tests.ut40.ut40,

	'it1':
	all_tests.it1.it1,
	'it2':
	all_tests.it2.it2,
	'it3':
	all_tests.it3.it3,
	'it4':
	all_tests.it4.it4,
	'it5':
	all_tests.it5.it5,
	'it6':
	all_tests.it6.it6,
	'it7':
	all_tests.it7.it7,
	'it8':
	all_tests.it8.it8,
	'it9':
	all_tests.it9.it9,
	'it10':
	all_tests.it10.it10,
	'it11':
	all_tests.it11.it11,
	'it12':
	all_tests.it12.it12,
	'it13':
	all_tests.it13.it13,
	'it14':
	all_tests.it14.it14,
	'it15':
	all_tests.it15.it15,
	'it16':
	all_tests.it16.it16,
	'it17':
	all_tests.it17.it17,
	'it18':
	all_tests.it18.it18,
	'it19':
	all_tests.it19.it19,
	'it20':
	all_tests.it20.it20,

	'pt1':
	all_tests.pt1.pt1,
	'pt2':
	all_tests.pt2.pt2,
	'pt3':
	all_tests.pt3.pt3,
	'pt4':
	all_tests.pt4.pt4,
	'pt5':
	all_tests.pt5.pt5,
	'pt6':
	all_tests.pt6.pt6,
	'pt7':
	all_tests.pt7.pt7,
	'pt8':
	all_tests.pt8.pt8,
	# 'pt9':
	# all_tests.pt9.pt9,
	'pt10':
	all_tests.pt10.pt10,
	'pt11':
	all_tests.pt11.pt11,
	'pt12':
	all_tests.pt12.pt12,
	'pt13':
	all_tests.pt13.pt13,
	'pt14':
	all_tests.pt14.pt14,
	'pt15':
	all_tests.pt15.pt15,
	'pt16':
	all_tests.pt16.pt16,
	'pt17':
	all_tests.pt17.pt17,
	'pt18':
	all_tests.pt18.pt18,
	'pt19':
	all_tests.pt19.pt19,
	'pt20':
	all_tests.pt20.pt20,
	'pt21':
	all_tests.pt21.pt21,
	'pt22':
	all_tests.pt22.pt22,
	'pt23':
	all_tests.pt23.pt23,
	'pt24':
	all_tests.pt24.pt24,
	'pt25':
	all_tests.pt25.pt25,


	# 'actions_grammar':
 #    all_tests.unit_test_actions.GrammarDeterminationTestCases,
 #    'actions_mouse':
 #    all_tests.unit_test_actions.MouseTestCases,
 #    'actions_selection':
 #    all_tests.unit_test_actions.SelectionTestCases,
 #    'actions_text_indent':
 #    all_tests.unit_test_actions.TextIndentTestCases,
 #    'actions_text_insert':
 #    all_tests.unit_test_actions.TextInsertTestCases,
 #    'application':
 #    all_tests.unit_test_application.ApplicationTestCases,
 #    'automatic_column_adjustment':
 #    all_tests.unit_test_automatic_column_adjustment.AutomaticColumnAdjustmentCases,
 #    'bookmarks':
 #    all_tests.unit_test_bookmarks.BookmarkTestCases,
 #    'brace_matching':
 #    all_tests.unit_test_brace_matching.BraceMatchingTestCases,
 #    'buffer_file':
 #    all_tests.unit_test_buffer_file.pathRowColumnTestCases,
 #    'copy_paste':
 #    all_tests.unit_test_copy_paste.CopyPasteTestCases,
 #    'curses_util':
 #    all_tests.unit_test_curses_util.CursesUtilTestCases,
 #    'file_manager':
 #    all_tests.unit_test_file_manager.FileManagerTestCases,
 #    'find':
 #    all_tests.unit_test_find_window.FindWindowTestCases,
 #    'execute':
 #    all_tests.unit_test_execute_prompt.ExecutePromptTestCases,
 #    'intention':
 #    all_tests.unit_test_intention.IntentionTestCases,
 #    'line_buffer':
 #    all_tests.unit_test_line_buffer.LineBufferTestCases,
 #    'misspellings':
 #    all_tests.unit_test_misspellings.MisspellingsTestCases,
 #    'parser':
 #    all_tests.unit_test_parser.ParserTestCases,
 #    'performance':
 #    all_tests.unit_test_performance.PerformanceTestCases,
 #    'prediction':
 #    all_tests.unit_test_prediction_window.PredictionWindowTestCases,
 #    'prefs':
 #    all_tests.unit_test_prefs.PrefsTestCases,
 #    'regex':
 #    all_tests.unit_test_regex.RegexTestCases,
 #    'selectable':
 #    all_tests.unit_test_selectable.SelectableTestCases,
 #    'startup':
 #    all_tests.unit_test_startup.StartupTestCases,
 #    'string':
 #    all_tests.unit_test_string.StringTestCases,
 #    'draw':
 #    all_tests.unit_test_text_buffer.DrawTestCases,
 #    'ui':
 #    all_tests.unit_test_ui.UiBasicsTestCases,
 #    'undo':
 #    all_tests.unit_test_undo_redo.UndoRedoTestCases,
}


def runTests(tests, stopOnFailure=False):
    """Run through the list of tests."""
    for test in tests:
        suite = unittest.TestLoader().loadTestsFromTestCase(test)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        if stopOnFailure and (result.failures or result.errors):
            return 1
    return 0


def usage():
    print('Help:')
    print('./unit_tests.py [--log] [[no] <name>]\n')
    print('  --help    This help')
    print('  --log     Print output from all_tests.log.* calls')
    print('  no        Run all tests except named tests')
    print('  <name>    Run the named set of tests (only)')
    print('The <name> argument is any of:')
    testNames = list(TESTS.keys())
    testNames.sort()
    for i in testNames:
        print(' ', i)


def parseArgList(argList):
    testList = list(TESTS.values())
    try:
        argList.remove('--help')
        usage()
        sys.exit(0)
    except ValueError:
        pass
    try:
        useAppLog = False
        argList.remove('--log')
        useAppLog = True
    except ValueError:
        pass
    if len(argList) > 1:
        if not (argList[1] == u"no" or argList[1] in TESTS):
            usage()
            sys.exit(-1)
        if argList[1] == u"no":
            for i in argList[2:]:
                del testList[testList.index(TESTS[i])]
        else:
            testList = []
            for i in argList[1:]:
                testList.append(TESTS[i])
    if useAppLog:
        all_tests.log.wrapper(lambda: runTests(testList, True))
    else:
        sys.exit(runTests(testList, True))


if __name__ == '__main__':
    parseArgList(sys.argv)
