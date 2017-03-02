# -*- coding: utf-8 -*-
import scrapy

class ImdbTvseriesSpider(scrapy.Spider):
    name = "imdb_tvseries"
    allowed_domains = ["http://www.imdb.com/"]
    start_urls = ['http://www.imdb.com/search/title?title_type=tv_series']

    def parse(self, response):
        for i in range(5):
            name = response.css("h3.lister-item-header a::text")[i].extract()
            year = response.css("h3.lister-item-header span.lister-item-year::text")[i].extract()
            rate = response.css("div.ratings-bar div strong::text")[i].extract()
            image = response.css("div.lister-item-image a img::attr(loadlate)")[i].extract()
            genre = response.css("p.text-muted span.genre::text")[i].extract().strip()
            vote = response.css("p.sort-num_votes-visible span::attr(data-value)")[i].extract()

            # iç sayfaya girip summary
            # response.css("div.summary_text::text").extract_first().strip()


            yield {
            	  "name": name,
                  "year": year[1:5],
                  "rate": rate,
                  "genre": genre,
                  "image": image,
                  "vote": vote
        	}
