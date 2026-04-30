# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:47:32 2026

@author: dipak
"""
# Taking prices from user

prices = []

n = int(input("Enter number of products: "))

for i in range(n):
    price = int(input("Enter price: "))
    prices.append(price)

total_bill = sum(prices)

print("Total bill amount:", total_bill)
