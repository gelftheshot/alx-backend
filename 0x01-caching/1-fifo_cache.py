#!/usr/bin/env python3
"""
    This caching system that use fif0
"""
import typing
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
        that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ constructer function that overides
            the orgianl function
        """
        super().__init__()
        self.key_queue = []

    def put(self, key, item):
        """
            assign to the dictionary cache_data the item value for the key
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    first_item = self.key_queue.pop(0)
                    del self.cache_data[first_item]
                    print("DISCARD:", first_item)
            if key not in self.key_queue:

                self.key_queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
            return the value in cache_data linked to key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
