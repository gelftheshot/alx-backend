#!/usr/bin/env python3
""" the first steps toward implementing pangation """
import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    ''' Return tuple containing pagination start index and end index. '''
    return ((page_size * (page - 1)), page_size * page)
