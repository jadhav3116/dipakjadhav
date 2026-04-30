# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:56:04 2026

@author: dipak
"""

purchases = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency = {}
for item in purchases:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print("Item frequency:", frequency)