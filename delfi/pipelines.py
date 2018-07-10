class DelfiPipeline(object):
    def process_item(self, item, spider):
        item['lead'] = [x for x in item['lead'] if x.strip()]
        item['lead'] = ' '.join(item['lead'])
        item['body'] = [x for x in item['body'] if x.strip()]
        item['body'] = '\n'.join(item['body'])
        return item
