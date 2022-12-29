# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import re
filename = input('What is your tex or txt file name?\n')
outputorfile = input('Do you want to make it a file or just output?[y]or[n]\n')
cited = []
# find all in-text citation of equations
cited = []
# find all in-text citation of equations

for idx, line in enumerate(open(filename)):
  if idx <= 2500:
    result = re.findall("ref\{(.*?)\}", line)
    if result:
      cited+=result


#
labelnotused = []
# find all labels not used
for idx, line in enumerate(open(filename)):
  if idx <= 2500:
    labels = re.findall("label\{(.*?)\}", line)
    for label in labels:
      if not (label in cited):
        labelnotused.append(label + ' in the line ' + str(idx + 1))

#
if outputorfile == 'y':
  text_file = open("labelnotused.txt", "w")

  # write string to file
  n = text_file.write('\n'.join(labelnotused))

  # close file
  text_file.close()
else:
  print('\n'.join(labelnotused))
