#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  name_list = []
  #name_dict = {}

  f = open(filename, 'rU') # Open file as read-write
  text = f.read()
  f.close()

  # Use Search Regex for Year
  match = re.search(r'Popularity\sin\s(\d\d\d\d)',text)
  if match:
      year = match.group(1)
      name_list.append(year)
  else:
      sys.stderr.write("No luck on year")
      sys.exit(1)

  # Use Findall Regex for Names + Ranks
  matches = re.findall(r'<td>(\d*)</td><td>(\w*)</td><td>(\w*)</td>',text)
  # matches is a list of tuples
  if matches:
      name_dict = dict([(b,a) for a,b,c in matches]) # adds male names
      name_dict.update(dict([(c,a) for a,b,c in matches] )) # updates with female
      #print(name_dict)
      for key in sorted(name_dict):
          value = name_dict[key]
          add_val = key + ' ' + value
          name_list.append(add_val)
      #print(name_list)
  else:
      sys.stderr.write("Cannot find names")
      sys.exit(1)
  return(name_list)


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  # the 0 element is the script, the 1 spot is the file
  # args is a list of strings, where each element is an html file

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1) # break out if no file passed

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]


  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
      name_list = extract_names(filename)
      text = '\n'.join(name_list)+'\n'
      if summary:
          #print(f"Making summary for {filename}")
          filename = filename + '.summary'
          sum_file = open(filename, "w")
          sum_file.write(text)
          sum_file.close()
      else:
          #print(f"Showing results for {filename}")
          print(text)

if __name__ == '__main__':
  main()


