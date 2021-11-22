#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:08:54 2017

@author: vijaypappu
"""

from random import randint


class BaseParents(object):
    def __init__(self):
        return self

    def generate(self, fitness_values):
        tot_pop = len(fitness_values) - 1
        father = randint(0, tot_pop)
        mother = randint(0, tot_pop)
        return (father, mother)
