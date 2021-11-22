#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:53:35 2017

@author: vijaypappu
"""

from .base_mutator import BaseMutator
from random import choice
from numpy import arange, array
from ..backend.common_utils import CommonUtils as cu


class BalanceMutator(BaseMutator):
    def __init__(self):
        pass

    def mutate(self, chromosome):

        bits = len(chromosome)
        bits_minus = bits - 1
        nnz_cols = chromosome.nonzero()[0]
        z_cols = list(set(arange(bits)) - set(nnz_cols))

        pointer1 = choice(nnz_cols)
        pointer2 = choice(z_cols)
        mask1 = "{0:b}".format(2 ** (bits_minus - pointer1))
        mask2 = "{0:b}".format(2 ** (bits_minus - pointer2))

        mask1_str = list('0' * (bits - len(mask1)) + mask1)
        mask2_str = list('0' * (bits - len(mask2)) + mask2)

        mask1_bool = array([int(x) for x in mask1_str], dtype=bool)
        mask2_bool = array([int(x) for x in mask2_str], dtype=bool)

        mutated_chromosome = ((chromosome ^ mask1_bool) ^ mask2_bool)
        return mutated_chromosome
