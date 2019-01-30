# All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'delfi'
SPIDER_MODULES = ['delfi.spiders']
NEWSPIDER_MODULE = 'delfi.spiders'
USER_AGENT = 'Friendly scraper'
DOWNLOAD_DELAY = 1
ITEM_PIPELINES = {'delfi.pipelines.DelfiPipeline': 300}
DOWNLOADER_CLIENT_TLS_METHOD = 'TLSv1.2'
