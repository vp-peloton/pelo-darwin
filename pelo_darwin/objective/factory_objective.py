#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:01:14 2017

@author: vijaypappu
"""

from .linear_objective import LinearObjective
import numpy as np


class FactoryObjective(object):

    @staticmethod
    def init(config):

        operator = config["operator"]

        if(operator == "linear"):
            cost_path = config["cost_path"]
            # delimiter = config["delimiter"]
            f = open(cost_path, 'r')
            cost_array = np.array([float(x) for x in f.read().split("\n")])
            return LinearObjective(cost_array)

        else:
            raise Exception("Invalid objective operator!")
