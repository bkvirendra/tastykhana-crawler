from scrapy.spider import BaseSpider
from scrapy.http import Request

from scrapy.selector import Selector

from bs4 import BeautifulSoup

from tastykhana.items import TastykhanaItem


class Tastykhana(BaseSpider):
    name = "tastykhana"
    allowed_domains = ["tastykhana.in"]

    def parse(self, response):
        soup = BeautifulSoup(response.body)
        result = []
        ids = []

        for li in soup.find_all(class_="search_result_row"):
            id = li.find(class_="rest_name").get("href").split("-")[-1]

            if id not in ids:
                item = TastykhanaItem()
                item['name'] = li.find(class_="rest_name").getText().strip()
                item['address'] = li.find(class_="address").getText().strip()
                item['timings'] = li.find(class_="overview").getText().strip()
                item['cuisine'] = li.find(class_="overview").getText().strip()
                item['logo'] = li.find(class_="lazy").get('src')
                item['id'] = id
                if li.find(class_="inb", title="Veg"):
                    item['veg'] = True
                else:
                    item['veg'] = False
                if li.find(class_="inb", title="Non-Veg"):
                    item['non_veg'] = True
                else:
                    item['non_veg'] = False
                result.append(item)
                ids.append(id)

        return result

    def start_requests(self):
        with open('/home/virendra/tastykhana/localities.txt', 'rb') as f:
            for line in f:
                yield Request("http://tastykhana.in/mumbai/" + repr(line)[1:-3], self.parse)
