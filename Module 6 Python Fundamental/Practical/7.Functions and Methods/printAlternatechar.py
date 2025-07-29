# Example: 9) Write a Python program to print every alternate character from the
# string starting from index 1.

def printString(name):
    for i in range(1, len(name), 2):
        print(name[i])

firatName = "Piyush"
printString(firatName)
