#!/usr/bin/python3
"""locked class module"""


class LockedClass:
    """class with no atribute or new instance
    except new instance is firstname"""
    
    __slots__ = ['first_name']
