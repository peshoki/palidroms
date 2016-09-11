import sys
from functions import *

'''
Main routine
'''
def main():
    for row in processPalidromCheck(0,1001):
        print '"decimal", "smallest base in which the number is a palindrome"'
        print ",".join(map(str, row))

if __name__ == "__main__":
    main()
