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

    def new_pipe(self, cmd, **options):
        """
        Open a new process pipe and 
        execute a new command

        :: Params
        :: - Positionals
        ::  + cmd : List of command and parameters to execute
        ::      - Syntax: [command, argument-1, argumnet-2, ...]
        ::      - Type: List
        ::  + options : Subprocess options kwargs
        ::      - Type: kwargs (Dictionary)
        """
        process = sp.Popen(cmd, **options)
        return process

    def is_alive(self, process):
        """
        Check if process is still alive

        :: Params
        :: - process : The process you wish to extract values from
        ::  Type: subprocess.Popen()
        
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

    def get_value(self, process): 
        """
        Get standard output from a process pipe

        :: Params
        :: - process : The process you wish to extract values from
        ::  Type: subprocess.Popen()
        """
        # Initialize Variables
        values = []
        alive_Check = self.is_alive(process)
        if(alive_Check == "Alive"):
            # If process is alive
            # Get standard output from process
            values.append(process.communicate())
        return values

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
