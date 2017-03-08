# -*- coding: utf-8 -*-
import scrapy

class ImdbTvseriesSpider(scrapy.Spider):
    name = "imdb_tvseries"
    #http://www.imdb.com/search/title?title_type=tv_series&page=1
    start_urls = []
    for c in range(1,3):
        start_urls.append('http://www.imdb.com/search/title?title_type=tv_series&page={}'.format(c))

    def parse(self, response):
        links = response.css("h3.lister-item-header a::attr(href)").extract()
        for l in links[:5]:
            l = response.urljoin(l)
            yield scrapy.Request(l, callback=self.parse_doc)

    def parse_doc(self, response):
        name = response.css("div.title_wrapper h1::text")[0].extract().strip()
        year = response.css("div.title_wrapper div.subtext a::text").extract_first()
        rate = response.css("div.ratings-bar div strong::text")[0].extract()
        image = response.css("div.poster a img::attr(src)").extract_first()
        genre = response.css("div.title_wrapper div.subtext a span::text").extract()
        vote = response.css("div.imdbRating a span.small::text").extract_first()
        summary = response.css("div.summary_text::text").extract_first().strip()

        yield {
              "name": name,
              "year": year[11:15],
              "rate": rate,
              "genre": genre,
              "image": image,
              "vote": vote,
              "summary": summary
        }
