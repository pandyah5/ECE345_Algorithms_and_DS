#!/usr/bin/env python
import sys
import csv

def insertion_sort(array):
  i = 0
  while (i < len(array)):
    j = i - 1
    value = array[i]
    while (j >= 0):
      if array[j][0] > value[0]:
        array[j + 1] = array[j]
        j -= 1
      else:
        break
    array[j + 1] = value
    i += 1
  
  for elem in array:
    print(*elem, sep=',')

if __name__ == "__main__":
    filename = sys.argv[1]
    array = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        index = 0
        for row in reader:
            array.append(row)
            index += 1
    insertion_sort(array[:10])
