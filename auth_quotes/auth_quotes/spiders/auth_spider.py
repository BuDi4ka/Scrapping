import scrapy
from ..items import AuthorItem


class AuthSpider(scrapy.Spider):
    name = "auth_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.css('div.quote'):
            author_page_link = quote.css('span a::attr(href)').get()
            if author_page_link:
                author_page_link = response.urljoin(author_page_link)
                yield scrapy.Request(author_page_link, callback=self.parse_author)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_author(self, response):
        author_item = AuthorItem()
        author_item['fullname'] = response.css('h3.author-title::text').get().strip()
        author_item['born_date'] = response.css('span.author-born-date::text').get()
        author_item['born_location'] = response.css('span.author-born-location::text').get().strip("in ")
        author_item['description'] = response.css('div.author-description::text').get().strip()

        yield author_item
