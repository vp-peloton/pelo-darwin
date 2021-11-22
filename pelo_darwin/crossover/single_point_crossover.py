#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:41:19 2017

@author: vijaypappu
"""

from .base_crossover import BaseCrossover
from numpy.random import randint
import numpy as np
import random


class SinglePointCrossover(BaseCrossover):

    def __init__(self, keep_count=True):
        self.keep_count = keep_count

    def offsprings(self, parents):

        """ return an array of bool arrays """

        # parents - array of bool arrays
        parent1 = parents[0]
        parent2 = parents[1]

        _, bits = parents.shape
        p = randint(1, (bits - 1))  # change to sample
        p_binary = "{0:b}".format((2**p - 1))

        mask1_str = list("{0:b}".format((2**bits - 2**p)))
        mask2_str = list("0" * (bits - len(p_binary)) + p_binary)

        mask1 = np.array([int(x) for x in mask1_str], dtype=bool)
        mask2 = np.array([int(x) for x in mask2_str], dtype=bool)

        offspring1 = (parent1 & mask1) | (parent2 & mask2)
        offspring2 = (parent1 & mask2) | (parent2 & mask1)

        offsprings = np.array([offspring1, offspring2], dtype=bool)

        if self.keep_count:
            offsprings = self.check_count_and_correct(parents, offsprings)
            return offsprings
        else:
            return offsprings

    def check_count_and_correct(self, parents, offsprings):

        offspring1, offspring2 = offsprings
        parents_count = np.sum(parents, axis=1)
        offsprings_count = np.sum(offsprings, axis=1)
        diff1, diff2 = parents_count - offsprings_count
        offspring1 = self.correct(offspring1, diff1)
        offspring2 = self.correct(offspring2, diff2)
        return np.array([offspring1, offspring2], dtype=bool)

    def correct(self, offspring, diff):
        if(diff > 0):
            z_indices = np.nonzero(offspring == False)[0]
            select_indices = random.sample(set(z_indices), diff)
            offspring[select_indices] = True
        elif(diff < 0):
            nnz_indices = np.nonzero(offspring == True)[0]
            select_indices = random.sample(set(nnz_indices), abs(diff))
            offspring[select_indices] = False
        return offspring
            
            
            
        
