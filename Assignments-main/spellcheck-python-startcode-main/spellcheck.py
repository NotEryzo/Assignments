# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time 

# Linear and Binary functions

def linearsearch(anArray, item):
    for i in range (len(anArray)):
        if anArray[i] == item:
            return i
    return -1

def binarysearch(anArray, item):
    lowerindex = 0
    upperindex = len(anArray) - 1

    while lowerindex <= upperindex:
        middleindex = (upperindex + lowerindex) // 2
        if item == anArray[middleindex]:
            return middleindex
        elif item < anArray[middleindex]:
            upperindex = middleindex - 1
        else:
            lowerindex = middleindex + 1

    return -1

# ---------------------------------------------------------------

# Main program function 

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("Assignments-main\spellcheck-python-startcode-main/data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("Assignments-main\spellcheck-python-startcode-main/data-files/AliceInWonderLand.txt")

    # Loop Menu

    while True:
        print("\nMain Menu")
        print("1. Spell Check a Word (Linear Search)")
        print("2. Spell Check a Word (Binary Search)")
        print("3. Spell Check Alice In Wonderland (Linear Search)")
        print("4. Spell Check Alice In Wonderland (Binary Search)")
        print("5. Exit")
        choice = int(input("Enter menu selection: "))

        # Find word using Linear Search

        if choice == 1:
            word = input("Please enter a word: ").lower()
            timeStart = time.time()
            output = linearsearch(dictionary, word)
            timeEnd = time.time()
            seconds = timeEnd - timeStart
            print("\nLinear Search starting...")
            if word in dictionary:
                print(f"{word} is in the dictionary at position {output}. ({seconds} seconds)")
            else:
                print(f"{word} is not in the dictionary. ({seconds} seconds)")


        # Find word using Binary Search

        elif choice == 2:
            word = input("Please enter a word: ").lower()
            timeStart = time.time()
            output = binarysearch(dictionary, word)
            timeEnd = time.time()
            seconds = timeEnd - timeStart
            print("\nBinary Search starting...")
            if word in dictionary:
                print(f"{word} is in the dictionary at position {output}. ({seconds} seconds)")
            else: 
                print(f"{word} is not in the dictionary. ({seconds} seconds)")
        
        # How many words are not found using Linear Search

        elif choice == 3:
            print("\nLinear Search starting...")
            count = 0
            timeStart = time.time()
            for i in range(len(aliceWords)):
                output = linearsearch(dictionary, aliceWords[i])
                if output == - 1:
                    count += 1
            timeEnd = time.time()
            seconds = timeEnd - timeStart
            print(f"The total number of words not found in the dictionary is: {count}. ({seconds} seconds)")

        # How many words are not found using Binary Search

        elif choice == 4:
            print("\nBinary Search starting...")
            count = 0
            timeStart = time.time()
            for i in range(len(aliceWords)):
                output = linearsearch(dictionary, aliceWords[i])
                if output == -1:
                    count += 1
            timeEnd = time.time()
            seconds = timeEnd - timeStart
            print(f"The total number of words not found in the dictionary is: {count}. ({seconds} seconds)")

        # End Menu Loop 

        elif choice == 5:
            break

        # Invalid Input 

        else :
            print("\nPlease select a number between (1-5)")
        

# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()
