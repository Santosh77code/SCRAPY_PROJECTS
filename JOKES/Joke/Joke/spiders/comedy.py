import scrapy
from ..items import JokeItem

class comedySpider(scrapy.Spider):
    name = "comedy"
    start_urls = [
        'http://www.laughfactory.com/jokes/family-jokes'       
    ]
    
    def parse(self , response):
        items = JokeItem()
        joke_text = response.css('div.joke-text p::text').extract()
        items['jokes_text'] = joke_text
            
        yield items