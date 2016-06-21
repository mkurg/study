#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import csv

import lxml
from lxml import etree

with open('raw_html/11-za-butylkoy-s-pasportom.html',
	encoding='utf-8') as proba:
	proba = prs
	root = etree.fromstring(proba)