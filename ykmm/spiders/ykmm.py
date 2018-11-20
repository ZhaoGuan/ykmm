# -*- coding: utf-8 -*-
# __author__ = "Gz"


import copy
import json
import logging

import scrapy
from scrapy_splash import SplashRequest
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from ykmm.items import YkmmItem


class MemeSpider(scrapy.Spider):
    name = "ykmm"

    # def parse(self, response):
    #     super(MemeSpider, self).parse(response)
    def __int__(self):
        self.base_url = "https://knowyourmeme.com/memes/popular"

    def start_requests(self):
        pages = range(1, 1000)
        for page in pages:
            url = "https://knowyourmeme.com/memes/popular/page/" + str(page)
            yield scrapy.Request(url=url, callback=self.memes_popular, dont_filter=True, meta={
                'page': page
            })

    def memes_popular(self, response):
        page = response.meta.get("page")
        if response.css("#infinite-scroll-wrapper>#entries>h3::text").extract() == []:
            populear_tags = response.css("#entries_list>table>tbody>tr>td>h2>a::text").extract()
            print(populear_tags)
            result = {"page": page, "tags": populear_tags}
            item = YkmmItem(result)
            yield item
