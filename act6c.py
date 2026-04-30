# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:01:39 2026

@author: dipak
"""
try:
    with open("complaints.txt", "r") as file:
        print("List of Complaints:\n")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Complaint file not found.")
