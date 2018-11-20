# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class YkmmPipeline(object):
    def __int__(self):
        self.result = {}

    def process_item(self, item, spider):
        page = item["page"]
        tags = item["tags"]
        self.result.update({page: tags})

    def spider_closed(self, spider):  # 爬虫结束时关闭文件
        print(self.result)
