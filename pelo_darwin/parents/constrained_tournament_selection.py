#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 13:58:39 2017

@author: vijaypappu
"""

from .base_parents import BaseParents
from random import sample


class ConstrainedTournamentSelection(BaseParents):

    def __init__(self, seed=1e6):

        self.seed = seed

    def generate(self, objective_values, 
                 feasibility, constraint_violation):
        # objective_values - array
        # feasibility - bool array
        # constraint_violation - array
        
        father = self.apply_constrained_tournament(objective_values,
                                                   feasibility, 
                                                   constraint_violation)
        mother = self.apply_constrained_tournament(objective_values,
                                                   feasibility, 
                                                   constraint_violation)
        return (father, mother)
    
    def apply_constrained_tournament(self, objective_values,
                                     feasibility, constraint_violation):
        chromosomes = len(objective_values)
        idx1, idx2 = sample(range(chromosomes), 2)
        f1, f2 = feasibility[[idx1, idx2]]
        if(f1 and f2):  # both are true
            parent = idx1 if objective_values[idx1] > objective_values[idx2] else idx2
        elif(f1 or f2):  # one of them is true
            parent = idx1 if f1 else idx2
        else:  # both are false
            parent = idx1 if constraint_violation[idx1] < constraint_violation[idx2] else idx2
            
        return parent