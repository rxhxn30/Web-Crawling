import scrapy
from ..items import AmazonscrapingItem

class Spider1Spider(scrapy.Spider):
    name = "spider1"
    page_number = 2
    start_urls = [
        'https://www.amazon.in/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_feature_three_browse-bin%3A9141482031&dc&qid=1685616327&ref=sr_ex_p_n_publication_date_0&ds=v1%3AgToGJr4YNgTz0DZ7yV4px9OR84zi1mGSRF%2BSLRBLe10'
    ]

    def parse(self, response):
        items = AmazonscrapingItem()


        # all_books = response.css('.s-list-col-right .sg-col-inner')


        book_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        book_author = response.css('.a-color-secondary .a-size-base.s-link-style').css('::text').extract()

        items['book_name'] = book_name
        items['book_author'] = book_author

        yield items

        next_page = 'https://www.amazon.in/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_feature_three_browse-bin%3A9141482031&dc&page=' + str(Spider1Spider.page_number) + '&qid=1685619817&ref=sr_pg_' + str(Spider1Spider.page_number)
        if Spider1Spider.page_number <=10:
            Spider1Spider.page_number+=1
            yield response.follow(next_page, callback=self.parse)

