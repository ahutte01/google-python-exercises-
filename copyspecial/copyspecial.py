#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
#import commands: removed after python2. use subprocess:
#https://docs.python.org/2/library/commands.html
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
    paths = []
    filenames = os.listdir(dir)
    for filename in filenames:
        match = re.search(r'\__\w*\__', filename)
        if match:
            fullpath = os.path.join(dir, filename)
            paths.append(fullpath)
    return paths

def copy_to(paths, dir):
    filenames = os.listdir(dir)
    new = os.path.abspath(paths)
    if not (os.path.exists(new)):
        makepath = os.makedirs(new)
        for file in filenames:
            if file.endswith(".txt"):
                shutil.copy(file, makepath)
    else: # folder exists
        for file in filenames:
            if file.endswith(".txt"):
                shutil.copy(file, paths)
    return

# Make a zipfile containing the file(s) in the folder where located
def zip_to(zipname, zippaths):
    # zippaths can be multiple paths to collect into zipfile
    cmd = "zip -j " + zipname + " " + "".join(zippaths)
    print("I am going to do this command: ", cmd)
    (status, output) = subprocess.getstatusoutput(cmd)
    # Status will be non-zero if there is a problem
    if status: # then error
        sys.stderr.write(output)
        sys.exit(1)
    return

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2] # inclusive, deletes args[0] (todir) and args[1] (the dir)

  tozip = ''
  if args[0] == '--tozip':
      # this is name of zipfile
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths = []
  if len(todir) >= 1:
      for arg in args:
          copy_to(todir, arg)
  elif len(tozip) >= 1 :
      for arg in args:
          zipped = zip_to(tozip, arg)
  else:
      for arg in args:
          path = get_special_paths(arg)
          paths.extend(path)
          text = '\n'.join(paths)
          print(text)


if __name__ == "__main__":
  main()


# code to run:
# python3.6 copyspecial.py /Users/amandahutter/Documents/PythonCode/Google/google-python-exercises/babynames/ /Users/amandahutter/Documents/PythonCode/Google/google-python-exercises/copyspecial/
# python3.6 copyspecial.py --todir /Users/amandahutter/Documents/PythonCode/Google/google-python-exercises/copyspecial/temp/foo /Users/amandahutter/Documents/PythonCode/Google/google-python-exercises/copyspecial
# python3.6 copyspecial.py --tozip temp.zip xyz__hello__.txt
