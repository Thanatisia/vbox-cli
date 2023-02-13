#!/usr/bin/env python3
"""
Run all Unit Test cases
"""
# Import Libraries
## Built-in
import os
import sys
import unittest
## Project
sys.path.append("src")
sys.path.append("src/lib")
import vbox
import cli

class UnitTest_VBox():
    def test_import_unittest_vbox(self):
        """
        Test import VirtualBox API
        """
        unittests_vbox = vbox.UnitTests() 
        if(unittests_vbox != None):
            # No Error
            print("[OK] Successfully imported VBox Library UnitTests class")
        else:
            # Error
            print("[Error] importing VBox library UnitTests class")

class UnitTest_CLI():
    def test_import_unittest_cli(self):
        """
        Test import CLI
        """
        unittests_cli = cli.UnitTests() 
        if(unittests_cli != None):
            # No Error
            print("[OK] Successfully imported CLI Library UnitTests class")
        else:
            # Error
            print("[Error] importing CLI library UnitTests class")

def setup():
    # Import classes
    global test_vbox, test_cli
    test_vbox = UnitTest_VBox()
    test_cli = UnitTest_CLI()

def main():
    print("==================================")
    test_vbox.test_import_unittest_vbox()
    test_cli.test_import_unittest_cli()
    print("==================================")

if __name__ == "__main__":
    setup()
    main()
