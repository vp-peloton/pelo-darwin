#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:40:26 2017

@author: vijaypappu
"""

import numpy as np
from .base_fitness import BaseFitness


class LinearFitness(BaseFitness):

    def __init__(self, cost_array):
        self.c = cost_array  # array

    def evaluate(self, population):

        # population: array of boolean arrays
        len_c = len(self.c)
        tot_pop = len(population)
        fitness_values = np.empty(tot_pop, dtype=float)  # array
        for idx in np.arange(tot_pop):
            chromosome = population[idx]
            if (len(chromosome) == len_c):
                fitness_values[idx] = sum(self.c[chromosome])
            else:
                raise Exception("""The chromosome dimensions do not match
                                the cost vector dimensions!""")
        return fitness_values
