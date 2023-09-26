import scrapy
from jobs_scraper.items import JobsScraperItem
from scrapy.loader import ItemLoader

class ReedSpider(scrapy.Spider):
    name = "reed"
    allowed_domains = ["reed.co.uk"]
    start_urls = ["https://www.reed.co.uk/jobs/business-analyst-jobs"]

    def parse(self, response):
        for job_link in response.xpath('//h2[contains(@class,"job-card_jobResultHeading__title")]/a/@href'):
            yield response.follow(job_link.get(), callback=self.parse_job)
    
    def parse_job(self, response):
        headers = response.xpath('//header[@class="job-header row"]')
        metadata = response.xpath('//div[contains(@class, "metadata container")]')

        job_info_loader = ItemLoader(item=JobsScraperItem(), selector=headers)

        job_info_loader.add_xpath("title", './/h1/text()')
        job_info_loader.add_xpath("posting_date", './/meta[@itemprop="datePosted"]/@content')
        job_info_loader.add_xpath("expiry_date", './/meta[@itemprop="validThrough"]/@content')
        job_info_loader.add_xpath("posted_by", './/span[@itemprop="name"]/text()')
        
        job_info_loader.selector = metadata
        job_info_loader.add_xpath("payment_currency", './/meta[@itemprop="currency"]/@content')
        job_info_loader.add_xpath("payment", './/span[@data-qa="salaryLbl"]/text()')
        job_info_loader.add_xpath("region", './/meta[@itemprop="addressRegion"]/@content')
        job_info_loader.add_xpath("country", './/meta[@itemprop="addressCountry"]/@content')
        job_info_loader.add_xpath("locality", './/span[@itemprop="addressLocality"]/text()')
        job_info_loader.add_xpath("type", './/span[@data-qa="jobTypeLbl"]/a/text()')
        
        job_info_loader.selector = response
        job_info_loader.add_xpath("desc", '//div[@class="description"]/descendant::*/text()')
        job_info_loader.add_xpath("id", '//p[@class="reference "]/text()')
        
        yield job_info_loader.load_item()