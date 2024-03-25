#!/usr/bin/python3
"""Test for the console"""

import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Class for testing console"""

    def setUp(self):
        """Set up the console for testing"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after testing"""
        del self.console

    def test_quit(self):
        """Test for the quit method"""
        self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test for the method EOF"""
        # Simulating EOF by passing an empty string
        self.assertTrue(self.console.onecmd(""))

if __name__ == '__main__':
    unittest.main()
