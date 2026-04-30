# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:59:56 2026

@author: dipak
"""
with open("attendance.txt", "a") as f:
    for i in range(3):
        name = input("Enter student name: ")
        status = input("Present/Absent: ")
        f.write(name + " - " + status + "\n")

print("Attendance recorded successfully.")
