#!python3
"""
CLI Subprocesses utility library
"""
import os
import sys
import subprocess as sp

class CLI():
    """
    Class handling CLI and Shell command/scripting support 
    in Python via subprocess
    """
    def __init__(self):
        self.class_name = "cli"
        self.description = "This class/library handles CLI and shell command/scripting support in python using subprocess"

    def new_pipe(self, command, **options):
        """
        Open a new process pipe and 
        execute a new command
        """
        process = sp.Popen(cmd, **options)
        return process

    def is_alive(self, process):
        """
        Check if process is still alive
        
        None: Alive, Not Terminated
        Else: Not Alive; Terminated
        """
        is_alive = process.poll()
        ret_Value = "Not Alive"

        # Check if process is alive
        if(is_alive is not None):
            # Alive
            ret_Value = "Alive"

        # Return result
        return ret_Value

class UnitTests():
    def test_import(self):
        """
        Test importing of class
        """
        cli = CLI()

def debug():
    unittest = UnitTests()
    unittest.test_import()

if __name__ == "__main__":
    debug()
