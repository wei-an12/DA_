import scrapy
      class spidery(scrapy.spider):
           name = "spidery"
           start_urls = ["input"]
           def parse(self,response):
                     css selector = 'img'
                     for x in response.css(css_selector):
                              newsel = '@src'
                              yield{
                                  "image Link":x.xpath(newsel).extract_first(),
                              }