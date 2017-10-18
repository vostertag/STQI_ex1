# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:36:07 2017

@author: victor
"""

from Sorter import Sorter

sorter = Sorter([5,9,7,2,6,1])
sorter.sort()
print(sorter.getToSort())
print(sorter.getSorted())
print(sorter.getNewPositions())
