#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv



with open("./tables/source_post1950_wordcount_by_words.csv", encoding="utf-8") as csv_file:
	reader = csv.DictReader(csv_file)
	with open("./tables/source_post1950_wordcount_by_genres.csv", "w", encoding="utf-8") as out_file:
		writer = csv.DictWriter(out_file, fieldnames=reader.fieldnames)
		writer.writeheader()
		for row in reader:
			try:
				if row['sphere'].startswith('публицистика'):
					print(row)
					#a = for val in row: a[val] = row[val]
					writer.writerow(row)
				elif int(row['words']) >= 80000:
					row['words'] = int(int(row['words']) / 2)
					writer.writerow(row)
					writer.writerow(row)
				else:
					writer.writerow(row)
			except ValueError:
				pass
