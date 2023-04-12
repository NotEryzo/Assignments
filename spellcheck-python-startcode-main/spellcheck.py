# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time

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

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("spellcheck-python-startcode-main/data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("spellcheck-python-startcode-main/data-files/AliceInWonderLand.txt")

    while True:
        print("\nMain Menu")
        print("1. Spell Check a Word (Linear Search)")
        print("2. Spell Check a Word (Binary Search)")
        print("3. Spell Check Alice In Wonderland (Linear Search)")
        print("4. Spell Check Alice In Wonderland (Binary Search)")
        print("5. Exit")
        choice = int(input("Enter menu selection: "))
        word = input("Please enter a word: ")

        if choice == 1:
            timeStart = time.time()
            output = linearsearch(dictionary, word)
            timeEnd = time.time()
            seconds = timeEnd - timeStart
            print("\nLinear Search starting...")
            if word in dictionary:
                print(f"{word} is in the dictionary at position {output}. ({seconds} seconds)")
            else:
                print(f"{word} is not in the dictionary. ({seconds} seconds)")

        if choice == 2:
            timeStart = time.time()
            output = binarysearch(dictionary, word)
            timeEnd = time.time()
            seconds = timeEnd - timeStart
            print("\nBinary Search starting...")
            if word in dictionary:
                print(f"{word} is in the dictionary at position {output}. ({seconds} seconds)")
            else: 
                print(f"{word} is not in the dictionary. ({seconds} seconds)")


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
