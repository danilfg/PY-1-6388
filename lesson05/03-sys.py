# SYS layer
import sys

# platform info
if sys.platform == 'darwin':
    my_lib = 'mac_os/code.py'
else:
    my_lib = 'win32/code.py'

sys.path.append(r'C:\PythonLibs')

# console arguments
arguments = sys.argv  # list of arguments

# argparse
import argparse

# argparse.ArgumentParser.add_argument()
# r"--file -f"
