#!/usr/bin/env python3

seq_file_obj = open("Python_06.fastq","r")

numberline = 0
numberchar = 0

for line in seq_file_obj:
  line = line.rstrip()
  lenght = len(line)
  numberline += 1
  numberchar += lenght

print(lenght,numberline,numberchar)

print(numberchar/numberline)
