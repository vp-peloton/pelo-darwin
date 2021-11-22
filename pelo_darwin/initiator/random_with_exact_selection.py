#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:05:22 2017

@author: vijaypappu
"""

import random
from .base_initiator import BaseInitiator
from numpy import array, arange, zeros, bool


class RandomWithExactSelection(BaseInitiator):

    def __init__(self, size, count, seed=1e6):
        self.size = size
        self.count = count
        self.seed = seed
        random.seed(self.seed)

    def generate(self):
        population = array(list(self.create_chromosomes()))
        return population

    def create_chromosomes(self):
        chromosomes, bits = self.size
        for idx in arange(chromosomes):
            chromosome = zeros(bits, dtype=bool)
            indices = random.sample(range(bits), self.count)
            chromosome[indices] = True
            yield chromosome
