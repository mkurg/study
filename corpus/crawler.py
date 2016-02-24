#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lxml
import urllib.request

def download_page(url):
	page = urllib.request.urlopen(url)