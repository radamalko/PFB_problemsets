#!/usr/bin/env python3
import sys

count = int(sys.argv[1])
if count > 0:
  message = "positive"
  print(count, message)
elif count < 0:
  message = "negative"
  print(count, message)
else:
  print('must be 0')

if count%2 == 1:
  message = "odd number"
  print(count, message)
elif count%3 == 0:
  message = "is devisible by 3"
  print(count, message)
else:
  print('must be even')

