#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

publ = 0
xud = 0
uchn = 0


with open("./tables/source_post1950_wordcount_by_words.csv", encoding="utf-8") as csv_file:
	reader = csv.DictReader(csv_file)
	with open("./tables/source_post1950_wordcount_by_genres.csv", "w", encoding="utf-8") as out_file:
		writer = csv.DictWriter(out_file, fieldnames=reader.fieldnames)
		writer.writeheader()
		for row in reader:
			try:
				if row['sphere'].startswith('публицистика'):
					publ += int(row['words'])
					if publ <= 29000000:
						writer.writerow(row)
				elif row['sphere'].startswith('художественная'):
					xud += int(row['words'])
					if xud <= 40000000:
						writer.writerow(row)
				elif row['sphere'].startswith('учебно-научная'):
					uchn += int(row['words'])
					if uchn <= 12000000:
						writer.writerow(row)
				else:
					writer.writerow(row)
			except ValueError:
				pass

