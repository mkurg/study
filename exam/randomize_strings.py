#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Надеемся тем самым обеспечить балансирование по словам, а также потенциально не брать части одного и того же произведения"""

import random
with open('./tables/source_post1950_wordcount_by_words.csv','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('./tables/source_post1950_wordcount_randomized.csv','w') as target:
    for _, line in data:
        target.write( line )