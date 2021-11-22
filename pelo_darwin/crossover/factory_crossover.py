#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 10:39:28 2017

@author: vijaypappu
"""

# from crossover import SinglePointCrossover
from .single_point_crossover import SinglePointCrossover
from .two_point_crossover import TwoPointCrossover
from .uniform_crossover import UniformCrossover


class FactoryCrossover(object):

    @staticmethod
    def init(config):

        operator = config["operator"]

        if(operator == "single_point"):
            return SinglePointCrossover()

        elif(operator == "two_point"):
            return TwoPointCrossover()

        elif(operator == "uniform"):
            return UniformCrossover()

        else:
            raise Exception("Invalid crossover operator!")
