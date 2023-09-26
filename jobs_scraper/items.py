# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

def extract_job_type(values):
    job_type = ""
    for desc in values:
        job_type += desc.strip() + " "
    
    return job_type.strip()

def extract_job_desc(job_desc):
    processed_desc = ""
    for section in job_desc:
        stripped_section = section.strip()
        if len(stripped_section) > 0:
            processed_desc += stripped_section + "\n"
    return processed_desc.strip()

def process_ref(value):
    return value[0].replace("Reference: ", "")

class JobsScraperItem(scrapy.Item):
    id = scrapy.Field(input_processor=process_ref)
    title = scrapy.Field()
    posting_date = scrapy.Field()
    expiry_date = scrapy.Field()
    posted_by = scrapy.Field()
    payment_currency = scrapy.Field()
    payment = scrapy.Field()
    locality = scrapy.Field()
    region = scrapy.Field()
    country = scrapy.Field()
    type = scrapy.Field(input_processor=extract_job_type)
    desc = scrapy.Field(input_processor=extract_job_desc)