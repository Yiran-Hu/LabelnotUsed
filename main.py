# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import re
filename = input('What is your tex or txt file name?\n')
outputorfile = input('Do you want to make it a file or just output?[y]or[n]\n')
cited = []
# find all in-text citation of equations
for idx, line in enumerate(open(filename)):
  if idx <= 2500:
    if "\\eqref{" in line:
      start = line.find("\\eqref{") + len("\\eqref{")
      end = line.find("}")
      temp = line[start:end]
      if temp!="":
        cited.append(temp)

    if "\\ref{" in line:
      start = line.find("\\ref{") + len("\\ref{")
      end = line.find("}")
      temp = line[start:end]
      if temp!="":
        cited.append(temp)

labelnotused = []
# find all labels not used
for idx, line in enumerate(open(filename)):
  if idx <= 2500:
    if "\\label{" in line:
      temp = line[line.find("\label{") + len("\label{"):line.find("}")]
      if temp!="":
        if not( temp in cited):
          labelnotused.append(temp+' in the line '+str(idx+1))
if outputorfile == 'y':
  text_file = open("labelnotused.txt", "w")

  # write string to file
  n = text_file.write('\n'.join(labelnotused))

  # close file
  text_file.close()
else:
  print('\n'.join(labelnotused))
