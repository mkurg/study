#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

y1960 = 0
y1970 = 0
y1980 = 0
y1990 = 0
y2000 = 0


with open("./tables/source_post1950_wordcount_by_genres.csv", encoding="utf-8") as csv_file:
	reader = csv.DictReader(csv_file)
	with open("./tables/source_post1950_wordcount_by_year.csv", "w", encoding="utf-8") as out_file:
		writer = csv.DictWriter(out_file, fieldnames=reader.fieldnames)
		writer.writeheader()
		for row in reader:
			try:
				if row['created'].startswith('196'):
					y1960 += int(row['words'])
					if y1960 <= 20000000:
						writer.writerow(row)
				elif row['created'].startswith('197'):
					y1970 += int(row['words'])
					if y1970 <= 20000000:
						writer.writerow(row)
				elif row['created'].startswith('198'):
					y1980 += int(row['words'])
					if y1980 <= 20000000:
						writer.writerow(row)
				elif row['created'].startswith('199'):
					y1990 += int(row['words'])
					if y1990 <= 20000000:
						writer.writerow(row)
				elif row['created'].startswith('200'):
					y2000 += int(row['words'])
					if y2000 <= 20000000:
						writer.writerow(row)
			except ValueError:
				pass
