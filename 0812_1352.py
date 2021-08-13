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
f.close()
"""

"""
テキストファイルへの書き出し(上書き)
f = open('out.txt', 'w', encoding='utf-8')
f.write("あいうえお\n")
f.write("12345")
f.close()
"""
"""
テキストファイルにリストでデータを渡す
f = open("out.txt", "a", encoding="utf-8")
data = ["\nかきくけこ\n", "67890"]
f.writelines(data)
f.close()
"""
"""
csvファイルへの書き出し(上書き)
f = open('out.csv', 'w', encoding='shift-jis')
f.write("あいうえお\n")
f.write("12345")
f.close()
"""
"""
csvファイルへリストで書き出し
aで実行すると既存データから一行空白開けて追加される
空白削除にはopenでnewline=""
import csv
f = open("out.csv", "a", encoding="shift-jis", newline="")
data = ["あいうえお", "12345"]
writer = csv.writer(f)
writer.writerow(data)
f.close()
"""
"""
csvファイルへ2次元リストで書き出し
2つめの[]が2行目になる
2行目の前に空白行を作らないためにはopenでnewline=""
import csv
f = open("out.csv", "a", encoding="shift-jis", newline="")
data = [["かきくけこ", "123456"], ["さしすせそ", "67890"]]
writer = csv.writer(f)
writer.writerows(data)
f.close()
"""