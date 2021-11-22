#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:05:22 2017

@author: vijaypappu
"""

from .random_selection import RandomSelection
from .random_with_upper_bound import RandomWithUpperBound
from .random_with_exact_selection import RandomWithExactSelection


class FactoryInitiator(object):

    @staticmethod
    def init(config):

        operator = config["operator"]

        if(operator == "random"):
            return RandomSelection()

        if(operator == "random_with_upper_bound"):
            return RandomWithUpperBound()

        if(operator == "random_with_exact_selection"):
            size = (int(x) for x in config["size"].split(","))
            count = int(config["count"])
            return RandomWithExactSelection(size, count)

        else:
            raise Exception("Invalid initial operator!")
