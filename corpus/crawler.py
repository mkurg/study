#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import re
import csv

initial_url = 'http://www.mr-info.ru/12017-ministr-postavil-pyaterku-nash-gorod-poluchil-pochetnuyu-gramotu-za-surdlimpiadu.html'

pages_number = 1800

all_urls = []
all_urls.append(initial_url)
downloaded_urls = []
downloaded_pages = {}

try:
	with open('downloaded.csv', encoding='utf-8') as downloaded_files:
		dw_files = csv.reader(downloaded_files, delimiter='\t')
		for row in dw_files:
			downloaded_urls.append(row[0])
except FileNotFoundError:
	pass

try:
	with open('urls.txt') as urls_file:
		for line in urls_file:
			all_urls.append(line.strip())
except FileNotFoundError:
	pass

def download_page(url):
	"""Downloads page by URL and puts it into the folder
	'html_pages'"""

	success = True
	try:
		page = urllib.request.urlopen(url)
	except HTTPError:
		success = False
		return [success, page]
	page = page.read()
	page = page.decode("cp1251")
	try:
		filename = re.search('([a-z0-9]*-)*[a-z0-9]*\.html', url).group(0)
	except AttributeError:
		success = False
		return [success, page]
	with open('raw_html/' + filename, 'w', encoding='utf-8') as local_file:
		local_file.write(page)
	if success == True:
		downloaded_urls.append(url)
		with open('downloaded.csv', 'a') as downloaded_files:
			dw_files = csv.writer(downloaded_files, delimiter='\t')
			dw_files.writerow([url, 'raw_html/' + filename])

	return [success, page]

def extract_urls(page):
	urls = re.findall('(http://www\.mr-info\.ru/([a-z0-9]*-)*[a-z0-9]*\.html)', page)
	for i in urls:
		all_urls.append(i[0])

for i in all_urls:
	if pages_number > 0:
		if i not in downloaded_urls:
			a = download_page(i)
			if a[0] == True:
				extract_urls(a[1])
				pages_number -= 1
				print(str(pages_number) + '\n' + i)

with open('urls.txt', 'w') as urls_file:
	for i in set(all_urls):
		urls_file.write(i + '\n')