#!/bin/bash

#if [ ! -d "venv" ]
#then
#    virtualenv venv
#fi
#
#. ./venv/bin/activate

sudo apt-get -y install -y libxml2 libxml2-dev

export PYTHONIOENCODING=UTF-8

pip install -r requirements.txt

#clear
rm -f page_url_list.txt
rm -f thread_url_list.txt
rm -f thread_text.txt

# crawling
scrapy crawl pages      # 爬页码的urls
scrapy crawl threads    # 爬Thread的urls
scrapy crawl posts      # 爬具体一个Thread上的文本
