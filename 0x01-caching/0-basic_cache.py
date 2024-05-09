#!/usr/bin/env python3
"""
    This caching system doesn’t have limit
"""
import typing
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
        that inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """
             assign to the dictionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
            return the value in cache_data linked to key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
