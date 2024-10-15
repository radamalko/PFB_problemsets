#!/usr/bin/env python3
import sys

name = 'rada'
print(name)
favcolor = 'blue'
print(favcolor)
activity = 'painting'
print(activity)
favanimal = 'dogs'
print(favanimal)

print(f"My name: {name}")

name = sys.argv[1]
favcolor = sys.argv[2]
activity = sys.argv[3]
favanimal = sys.argv[4]
print('my name is', name, 'my favorite color is', favcolor, 'my favorite activity is', activity, 'my favorite animals are', favanimal)

