A scrapy crawler for information from job postings. Current implementation supports Reed.co.uk.

Usage applications include:
* Analysing the jobs market
* Create customised alerts

How to Run
1. Create a virtual environment
2. Install the required packages: pip install -r requirements.txt
3. Run the spider to fetch data using a command like: scrapy crawl reed -O output_file.csv

To do by priority:
* Investigate empty rows in output. They are currently being dropped.
* Format the expiry_date field
* Expand the payment field into a number of fields: min, max, period etc?
* Add multipage crawling and stopping point