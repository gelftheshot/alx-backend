#!/usr/bin/python3
''' MRU Caching
    Create a class MRUCache that inherits from BaseCaching
'''

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''
    An MRU Cache.
    '''

    def __init__(self):
        ''' constructor '''
        super().__init__()
        self.key_queue = []

    def put(self, key, item):
        '''
        Add key/value pair to cache data.
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.key_queue:
                self.key_queue.append(key)
            else:
                self.key_queue.append(
                    self.key_queue.pop(self.key_queue.index(key))
                )
            if len(self.key_queue) > BaseCaching.MAX_ITEMS:
                discard = self.key_queue.pop(-1)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        '''
        Return value stored in `key` key of cache.
        If key is None or does not exist in cache, return None.
        '''
        if key is not None and key in self.cache_data:
            self.key_queue.append(
                self.key_queue.pop(self.key_queue.index(key))
            )
            return self.cache_data[key]
        return None
