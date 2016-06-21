#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import xlrd
import csv

import pandas as pd

'''
def csv_from_excel(file):

    wb = xlrd.open_workbook("./tables/" + file)
    sh = wb.sheet_by_name(u'Лист1')
    csv_file = open(file[:-4] + 'csv', 'wb')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    csv_file.close()
'''

def csv_from_excel(file):
	data_xls = pd.read_excel("./tables/" + file, u'Лист1', index_col=None)
	data_xls.to_csv("./tables/" + file[:-4] + '.csv', encoding='utf-8')

for root, dirs, files in os.walk("./tables", topdown=False):
	for name in files:
		csv_from_excel(name)
