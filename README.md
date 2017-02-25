# ScrapyTutorial
Scrapy (/ˈskreɪpi/ SKRAY-pee) is a free and open source web crawling framework, written in Python. Originally designed for web scraping, it can also be used to extract data using APIs or as a general purpose web crawler.


### Installation

Install dependency packages

```sh
$ pip install -r requirements.txt
```


### Run Spider

running spiders

```sh
$ scrapy crawl quotes
$ scrapy crawl author
```
Corresponding output files `quotes_file.csv` and `author_file.csv` will be created at project root folder