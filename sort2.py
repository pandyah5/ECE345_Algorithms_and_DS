#!/usr/bin/env python
import sys
import csv

def bubble_sort(array):
  while (True):
    changes = 0
    for i in range(0, len(array) - 1):
      if (array[i][0] > array[i + 1][0]):
        array[i], array[i + 1] = array[i + 1], array[i]
        changes += 1
    if (changes == 0):
      break

  for elem in array:
    print(*elem, sep=',')
    
if __name__ == "__main__":
    filename = sys.argv[1]
    array = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            array.append(row)
    bubble_sort(array)
