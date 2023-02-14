#!python3
## Import Libraries
### Built-In
import os
import sys
from subprocess import Popen, PIPE

### External Libraries
import virtualbox as vbox

### Personal Libraries
import lib.cli as cli

class VirtualBox():
    def __init__(self):
        self.class_name = "VirtualBox"
        self.clihelper = cli.CLI()

    def list_vms(self):
        """
        List all running Virtual Machines
        """
        proc = self.clihelper.new_pipe(["vboxmanage", "list", "vms"], stdin=PIPE, stdout=PIPE)
        # Get values
        all_vms = self.clihelper.get_value(proc)
        print("Virtual Machines : {}".format(all_vms))

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
