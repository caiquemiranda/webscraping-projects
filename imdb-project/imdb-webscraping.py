import scrapy


class ImdbScreaping(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top']

    def parse(self, response):
        for title in response.css('td.titleColumn'):
            yield {
                'title': title.css('a::text').get(),
                'year': title.css('span.secondaryInfo::text').get(),
                'rating': title.css('td.ratingColumn::text').get(),
            }
        next_page = response.css('div.desc a::attr(href)').get()
        ''' if next_page is not None:
            yield response.follow(next_page, self.parse)'''