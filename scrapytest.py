class Spidery(scrapy.spider):
    name = "spidery"
    start_urls = ['http://8.8.8.8']
    def parse(self, response):
        xpath_selector ='//img'
        for x in response.xpath(xpath_selector):
            newsel ='@src'
            yield{
                  'image Link':x.xpath(newsel).extract_first(),

            }

        #To recurse next page
    Page_selector = '.next a ::attr(href)'
        name_page = response.css(page_selector).extract_first()
        if next_page:
            yield scrappy.Request(
                  response.urljoin(next_page),
                  callback=self.parse
            )