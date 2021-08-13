# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 13:52:02 2021

@author: erina
"""
"""
テキストファイル読込
f = open("practice.txt", "r", encoding="utf-8")
data = f.readlines()
f.close()
print(data[2].strip)
"""

"""
csvファイル読込
import csv
f = open("input.csv", encoding="shift-jis")
data = csv.reader(f, delimiter=",")
for row in data:
    print(row)
"""

"""
テキストファイルへの書き出し(上書き)
f = open('out.txt', 'w', encoding='utf-8')
f.write("あいうえお\n")
f.write("12345")
f.close
"""