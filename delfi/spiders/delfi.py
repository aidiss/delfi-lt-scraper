from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DelfiSpider(CrawlSpider):
    name = 'crawler'
    allowed_domains = ['delfi.lt']
    start_urls = ['http://www.delfi.lt/']

    rules = (
        Rule(LinkExtractor(restrict_css='h3.headline-title a'),
             callback='parse_item',
             follow=True),
        Rule(LinkExtractor(restrict_css='.paging'),
             follow=True),
    )

    def parse_item(self, r):
        i = {}
        i['lead'] = r.css('.delfi-article-lead *::text').extract()
        i['image'] = r.css(
            'div.article-image div.image-article a.fancybox img').xpath('@src').extract()
        i['body'] = r.xpath('//div[@itemprop="articleBody"]//text()').extract()
        return i
