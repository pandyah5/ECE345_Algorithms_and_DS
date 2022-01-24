#!/usr/bin/env python
import sys
import csv

def merge_sort(array):
  if (len(array) == 1):
    return array
  left = merge_sort(array[0:int(len(array)/2)])
  right = merge_sort(array[int(len(array)/2):])
  result = merge(left, right)
  return result

def merge(left, right):
  i = 0
  j = 0
  result = []
  while (True):
    if (i < len(left) and j < len(right)):
      if (left[i][0] > right[j][0]):
        result.append(right[j])
        j += 1
      else:
        result.append(left[i])
        i += 1
    elif (i < len(left)):
      result.append(left[i])
      i += 1
    elif (j < len(right)):
      result.append(right[j])
      j += 1
    else:
      break
  return result
    
if __name__ == "__main__":
    filename = sys.argv[1]
    array = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        index = 0
        for row in reader:
            array.append(row)
            index += 1
    result = merge_sort(array[:10])
    for elem in result:
        print(*elem, sep=',')
