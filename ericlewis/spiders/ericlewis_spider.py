import scrapy


class EricLewisSpider(scrapy.Spider):
    name = "ericlewis"

    def start_requests(self):
        urls = [
            'https://redding-real-estate.com/mls/search?sqrft=1500&mprice=400000&sort=price&rpp=500',
            # 'http://quotes.toscrape.com/page/1/',
            # 'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(f'Testing output:')
        for table in response.xpath('body/div/table/tr[1]/td/div[@class="mlsResultItemDiv"]/table'):
            # print(div.getall())
            yield {
                'details': table.xpath('tr[1]/td[3]/span').get(),
                'price': table.xpath('tr[1]/td[4]').get()
            }

        # for quote in response.css('div.quote'):
        #     yield {
        #         'text': quote.css('span.text::text').get(),
        #         'author': quote.css('small.author::text').get(),
        #         'tags': quote.css('div.tags a.tag::text').getall(),
        #     }
        # page = response.url.split("/")[-2]
        # filename = f'ericlewis-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
        # /html/body/div/table/tbody/tr[1]/td/div[268]/table/tbody/tr[1]/td[4]

        #  response.xpath('body/div/table/tr[1]/td/div[1]')
        