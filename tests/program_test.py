from program import all_programs, PyCharm, Bash, RubyMine, IntelliJ, Xcode, Sublime_Key
import unittest


class TestPrograms(unittest.TestCase):
    def test_all_programs(self):
        current_all_programs = [Sublime_Key, Xcode, IntelliJ, RubyMine, Bash, PyCharm]
        self.assertEqual(current_all_programs, all_programs, "Did you add a new program?")