import scrapy
from ScrapyTutorial.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            # yield {
            #     'text': quote.css('span.text::text').extract_first(),
            #     'author': quote.css('span small::text').extract_first(),
            #     'tags': quote.css('div.tags a.tag::text').extract(),
            # }
            records = QuotesItem()
            records['text'] = quote.css('span.text::text').extract_first()
            records['author'] = quote.css('span small::text').extract_first()
            records['tags'] = quote.css('div.tags a.tag::text').extract()

            yield records

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
