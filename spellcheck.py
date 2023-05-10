# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time 
import math

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

# Load data files into lists
dictionary = loadWordsFromFile("data-files/dictionary.txt")
aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

def linearSearch(anArray, item):
  for el in range(0, len(anArray)):
    if (anArray[el] == item):
      return el
  return -1
  
def binarySearch(anArray, item):
  lowerIndex = 0
  upperIndex = len(anArray) - 1

  while lowerIndex <= upperIndex:
    middleIndex = (lowerIndex + upperIndex) // 2
    if item == anArray[middleIndex]:
      return middleIndex
    elif item < anArray[middleIndex]:
      upperIndex = middleIndex - 1
    else:
      lowerIndex = middleIndex + 1
  return -1

# Main Menu

# Main Programming Loop
loop = True
while loop:
  # Print Main Menu
  print("\nMain Menu")
  print("1: Spell Check a Word (Linear Search)")
  print("2. Spell Check a Word (Binary Search)")
  print("3. Alice in Wonderland (Linear Search)")
  print("4. Alice in Wonderland (Binary Search)")
  print("5. Exit")

  # User Input for Menu
  selection = input("Enter selection (1-5): ")

  if (selection == "1"): 
    print("Spell Check a Word (Linear Search)")
    userInput = input("Enter a word to check: ").lower()
    searchStartTime = time.time()
    search = linearSearch(dictionary, userInput)
    searchEndTime = time.time()
    if search == -1:
      print(userInput + " was not found at position")  
    else:
      print(userInput + " was found at position " + str(search) + " time taken by linear search is = ",(searchEndTime-searchStartTime))
  
  elif (selection == "2"):
    print("Spell Check a Word (Binary Search)")
    userInput = input("Enter a word to check: " ).lower()
    searchStartTime = time.time()
    search = binarySearch(dictionary, userInput)
    searchEndTime = time.time() 
    if search != -1:
      print(userInput + " was found at position " + str(search) + " time taken by binary search is = ",(searchEndTime-searchStartTime))
    else:
      print(userInput + " was not found")
  
  elif (selection == "3"):
    print("Alice in Wonderland Linear Search")
    count = 0
    searchStartTime = time.time()
    for i in range(len(aliceWords)):
      search = linearSearch(dictionary, aliceWords[i].lower())
      if search == -1:
        count += 1
    searchEndTime = time.time() 
    print("Number of words not found in dictionary " + str(count) + " : ",(searchEndTime-searchStartTime))
      
  elif (selection == "4"):
    print("Alice in Wonderland Binary Search")
    count = 0
    searchStartTime = time.time()
    for i in range(len(aliceWords)):
      search = binarySearch(dictionary, aliceWords[i].lower())
      if search == -1:
        count += 1
    searchEndTime = time.time() 
    print("Number of words not found in dictionary " + str(count) + " : ",(searchEndTime-searchStartTime))
          
  elif (selection == "5"):
    print("Exit")
    loop = False