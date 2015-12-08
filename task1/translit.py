# -!- encoding: utf-8 -!-
import re
import sys
import csv

a = {}
with open('georgian.csv', 'r', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in spamreader:
        a[re.sub('\s', '', row[0])] = re.sub('\s', '', row[2])
b = ''
with open('test.txt') as inp:
    for line in inp:
        for char in line:
            try:
                b += re.sub(char, a[char], char)
            except KeyError:
                b += char
with open('out.txt', 'w') as out:
    out.write(str(b))