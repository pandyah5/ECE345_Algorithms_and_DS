#!/usr/bin/env python3
import sys

# Get function arguments
file_name = str(sys.argv[1])
cust_pass = str(sys.argv[2])

# Define a hash function
def hashFunction(password, size):
  i=0
  sum = 0
  for character in password:
    sum = sum + (i+1)*ord(password[i])
    i += 1
  return sum%(size-1)

# Parse the password list
file = open(file_name,"r")

passwordList = []
counter = 0
passwords=file.readline()

while passwords:
  passwordList.append(passwords)
  passwordList[counter]=passwordList[counter][:-1]
  counter += 1
  passwords=file.readline()

hashTableSize = 12289 # Explanation in report (389)

# Add elements to the hastable
hashTable = []
for _ in range(hashTableSize):
  hashTable.append(None)

index = 0
for password in passwordList:
  hashValue = hashFunction(passwordList[index],hashTableSize)
  while hashTable[hashValue]!=None :
   hashValue += 1
   if hashValue>hashTableSize - 1:
     hashValue = hashValue - hashTableSize+1
  hashTable[hashValue] = passwordList[index]
  index += 1

# now hashTable has been created
# now we have to check if entered password exists in hashTable

inputString = cust_pass

# Error checking for length
if len(inputString)<6:
  print("\nINVALID")
  sys.exit("Password is too short. Must be atleast 6 characters")

if len(inputString)>12:
  print("\nINVALID")
  sys.exit("Password is too long. Must be less than 12 characters")

# Error checking for invalid character
alpha_range_caps = range(65, 91)
alpha_range_small = range(97, 123)
num_range = range(48, 58)

for char in inputString:
    if ord(char) not in alpha_range_caps:
        if (ord(char) not in alpha_range_small):
            if (ord(char) not in num_range):
                print("\nINVALID")
                sys.exit("Password contains invalid characters")
            else:
                pass
        else:
            pass
    else:
        pass

# Hash value of the new password
hashValue = hashFunction(inputString,hashTableSize)

# Find value in hash table
while hashTable[hashValue]!=None :
  if hashTable[hashValue] == inputString:
    #This means same password exists in hashTable
    print("\nINVALID")
    sys.exit("Same password found in data")
  if hashValue>hashTableSize - 1:
     hashValue = hashValue - hashTableSize+1

  hashValue += 1

# Find reverse value in hashtable
checkValue = hashFunction(inputString[::-1],hashTableSize)
while hashTable[checkValue]!=None :
  if hashTable[checkValue] == inputString[::-1]:
    #This means reverse password exists in hashTable
    print("\nINVALID")
    sys.exit("Reverse password found in data")
  if checkValue>hashTableSize - 1:
    checkValue = checkValue - hashTableSize+1

  checkValue += 1

# If we reach here, this means neither password nor reverse of it exists in the hashTable.
# ADD PASSWORD IN passwords.txt

print("\nVALID")

with open(file_name, "a") as myfile:
    myfile.write(inputString)
