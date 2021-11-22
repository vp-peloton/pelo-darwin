#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:39:34 2017

@author: vijaypappu
"""

from .base_parents import BaseParents
from numpy import arange
from random import randint
from ..backend.common_utils import CommonUtils as cu


class RankSelection(BaseParents):

    def __init__(self, seed=1e6):

        self.seed = seed

    def generate(self, fitness_values):
        # fitness_values - array 
        total_pop = len(fitness_values)
        idx_pop = [(idx, fitness_values[idx]) for idx in arange(total_pop)]
        fv_sorted = sorted(idx_pop, key=lambda value: value[1])

        fibannaci = [0]
        rank_to_pop = {}
        for idx, fv in enumerate(fv_sorted, 1):
            value = idx + fibannaci[idx - 1]
            fibannaci.append(value)
            rank_to_pop[idx] = fv

        fibannaci = fibannaci[1:]
        max_limit = 0.5 * (total_pop * (total_pop + 1))
        father_rand = randint(1, max_limit)
        mother_rand = randint(1, max_limit)
        father_rank = cu.find_rank(fibannaci, father_rand)
        mother_rank = cu.find_rank(fibannaci, mother_rand)

        while(father_rank == mother_rank):
            mother_rand = randint(1, max_limit)
            mother_rank = cu.find_rank(fibannaci, mother_rand)

        father_ind = rank_to_pop[father_rank][0]
        mother_ind = rank_to_pop[mother_rank][0]

        return (father_ind, mother_ind)
