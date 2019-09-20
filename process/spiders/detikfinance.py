import scrapy
class JudulSpider(scrapy.Spider):
    name = "judul"
    def start_requests(self):
        urlBasang = "https://finance.detik.com"
        yield scrapy.Request(url = urlBasang, callback = self.parse)
    def parse(self, response):
        newCsv = open('data_information/judulartikel.csv', 'a')
        for j in response.xpath('//h2'):
            title_to_save = j.xpath('text()').extract_first()
           
            if len(title_to_save.replace(" ","") ) > 1:
                newCsv.write(title_to_save+ "\n")
        newCsv.close()