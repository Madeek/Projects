import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider(scrapy.Spider):

    name = 'myspider'
    start_urls = ['https://example.com']

    def parse(self, response):

        # Extracting data from the response using XPath or CSS selectors
        data = response.xpath('//h2[@class="article-title"]/text()').getall()

        # Print the extracted data
        for item in data:

            print(item)

# Running the spider
if __name__ == "__main__":

    process = CrawlerProcess()
    process.crawl(MySpider)
    process.start()
