#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:36:36 2017

@author: vijaypappu
"""

from .base_parents import BaseParents


class TournamentSelection(BaseParents):

    def __init__(self):
        return self



#    def tournament(self, fits_populations):
#        alicef, alice = self.select_random(fits_populations)
#        bobf, bob = self.select_random(fits_populations)
#        return alice if alicef > bobf else bob