#!/usr/bin/python3
'''
LFU Caching: Create a class LFUCache that inherits from BaseCaching
'''
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''
    An LFU cache.
    '''
    def __init__(self):
        ''' Initialize class instance. '''
        super().__init__()
        self.key_queue = []
        self.uses = {}

    def put(self, key, item):
        '''
        Add key/value pair to cache data.
        '''
        if key is not None and item is not None:
            if (len(self.key_queue) == BaseCaching.MAX_ITEMS and
                    key not in self.key_queue):
                discard = self.key_queue.pop(
                    self.key_queue.index(self.findLFU())
                )
                del self.cache_data[discard]
                del self.uses[discard]
                print('DISCARD: {:s}'.format(discard))
            self.cache_data[key] = item
            if key not in self.key_queue:
                self.key_queue.append(key)
                self.uses[key] = 0
            else:
                self.key_queue.append(
                    self.key_queue.pop(self.key_queue.index(key))
                )
                self.uses[key] += 1

    def get(self, key):
        '''
        Return value stored in `key` key of cache.
        '''
        if key is not None and key in self.cache_data:
            self.key_queue.append(
                self.key_queue.pop(self.key_queue.index(key))
            )
            self.uses[key] += 1
            return self.cache_data[key]
        return None

    def findLFU(self):
        '''
        Return key of least frequently used item in cache.
        '''
        items = list(self.uses.items())
        freqs = [item[1] for item in items]
        least = min(freqs)

        lfus = [item[0] for item in items if item[1] == least]
        for key in self.key_queue:
            if key in lfus:
                return key
