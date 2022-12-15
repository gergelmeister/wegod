import sys
sys.path.append('/Users/macbookbro/PycharmProjects/wegod_bot')

import scrapy
import users_db
from scrapy.crawler import CrawlerProcess


class MironlineRateSpider(scrapy.Spider):
    name = 'mironline_rate'
    allowed_domains = ['mironline.ru']
    start_urls = ['https://mironline.ru/support/list/kursy_mir/']

    def parse(self, response):
        KZT_path = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/div[2]/table/tbody/tr[5]/td[2]/span/p/text()'
        scraped_info = float(response.xpath(KZT_path).extract()[0].strip().replace(',', '.'))

        users_db.update_rate('KZT', scraped_info)

        yield scraped_info


    def startcrawler(self):
        process = CrawlerProcess(settings={
            "FEEDS": {
                "items.json": {"format": "json"},
            },
        })

        process.crawl(MironlineRateSpider)
        process.start()




