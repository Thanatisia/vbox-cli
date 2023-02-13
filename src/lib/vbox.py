#!python3
## Import Libraries
### Built-In
import os
import sys
from subprocess import Popen, PIPE

### External Libraries
import virtualbox as vbox

class VirtualBox():
    def __init__(self):
        self.class_name = "VirtualBox"

class UnitTests():
    def test_import(self):
        """
        Test importing of class
        """

def debug():
    unittest = UnitTests()
    unittest.test_import()

if __name__ == "__main__":
    debug()
