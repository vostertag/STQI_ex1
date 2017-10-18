# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:25:25 2017

@author: victor
"""

from pathlib import Path
import sys

class Input:
    
    def __init__(self, userInput=None):
        if userInput == None:
            userInput = input('Type in an array using "," as a seperator or a file name: ')
            self.checkString(userInput)
        elif type(userInput) is list:
            self.checkArray(userInput)
        elif type(userInput) is str:
            self.checkString(userInput)
        else:
            raise TypeError("Invalid Input")
        
        
    def checkString(self, userInput):
        try:
            self.array = [int(x) for x in userInput.split(",")]
        except:
            file = Path(userInput)
            if file.is_file():
                if not userInput.endswith(".txt"):
                    raise ValueError("File must be .txt")
                else:
                    file = open(userInput,'r').read()
                    try:
                        self.array = [int(x) for x in file.split(" ")]
                    except:
                        raise ValueError("The file is not in the right format")
            else:
                raise ValueError("Something went wrong when you typed in the array or the file does not exist")
    
    def checkArray(self, userInput):
        if any(not isinstance(x, int) for x in userInput):
            raise ValueError("The array should only have ints.")
        else:
            self.array = userInput
            
    def getArray(self):
        return self.array
        
            