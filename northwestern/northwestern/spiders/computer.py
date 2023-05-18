import scrapy
from ..items import NorthwesternItem


class ComputerSpider(scrapy.Spider):
    name = 'computer'
    
    def start_requests(self):
        url = 'https://www.mccormick.northwestern.edu/computer-science/people/faculty.html'

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

        # try:
        items = NorthwesternItem()

        items['name'] = response.css("h1::text").get()
        title = response.css(".title::text").get()
        if "Assistant" in title :
            items['title'] = 'Assistant Professor'
        elif "Associate" in title :
            items['title'] = 'Associate Professor'
        else:
            items['title'] = 'Professor'
        items['email'] = response.css(".mail_link::attr(href)").get()
        items['program_id'] = 7
        items['school_id'] = 501
        items['research_area'] = None
        items['link'] = response.url
        items['image'] = "https://www.mccormick.northwestern.edu/" + response.css("#faculty-profile-left img::attr(src)").get().replace("../../../","")

        yield items
            
        # except:
        #     items = NorthwesternItem()

        #     items['name'] = response.css("h2::text").get().replace("\xa0B"," ")
        #     items['title'] = 'Professor'
        #     items['email'] = response.css(".link-box li:nth-child(1) a::attr(href)").get().replace("mailto:","")
        #     items['program_id'] = 7
        #     items['school_id'] = 501
        #     items['research_area'] = None
        #     items['link'] = response.url
        #     items['image'] = "https://www.mccormick.northwestern.edu/" + response.css(".photo::attr(src)").get().replace("../../../","")

        #     yield items