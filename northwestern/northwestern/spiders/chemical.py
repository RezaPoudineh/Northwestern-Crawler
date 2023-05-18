import scrapy
from ..items import NorthwesternItem


class ChemicalSpider(scrapy.Spider):
    name = 'chemical'
    
    def start_requests(self):
        url = 'https://www.mccormick.northwestern.edu/chemical-biological/people/faculty/'


        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        print('\n+++++++++++++++++++++++++++++++++++\n')
        urlvalue = response.css("h3 a::attr(href)").extract()
        for i in urlvalue:
            yield scrapy.Request(
                url= i,
                method='GET',
                callback=self.info
            )

    def info(self, response):

        items = NorthwesternItem()

        items['name'] = response.css("h1::text").get()
        title = response.css(".title::text").get()
        if "Assistant" in title :
            items['title'] = 'Assistant Professor'
        elif "Associate" in title :
            items['title'] = 'Associate Professor'
        else:
            items['title'] = 'Professor'
        items['email'] = response.css(".mail_link::attr(href)").get().replace("mailto:","")
        items['program_id'] = 5
        items['school_id'] = 501
        items['research_area'] = None
        items['link'] = response.url
        items['image'] = "https://www.mccormick.northwestern.edu/" + response.css("#faculty-profile-left img::attr(src)").get().replace("../../../","")

        yield items