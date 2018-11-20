# -*- coding: utf-8 -*-
# __author__ = 'Gz'

from scrapy import cmdline

name = 'ykmm'
cmd = 'scrapy crawl {0} -o test.csv'.format(name)
# cmd = 'scrapy crawl {0} '.format(name)
cmdline.execute(cmd.split())

