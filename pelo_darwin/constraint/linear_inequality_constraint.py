#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 22:59:18 2017

@author: vijaypappu
"""

from .base_constraint import BaseConstraint
import numpy as np


class LinearInequalityConstraint(BaseConstraint):

    def __init__(self, A, b):
        # A - ndarray, b - array
        self.A = A
        self.b = b

    def evaluate_constraints(self, population):
        feasibility = np.empty(len(population), dtype=bool)        
        constraint_violation = np.empty(len(population))
        for idx, chromosome in enumerate(population):
            constraint_values = np.matmul(chromosome, np.transpose(self.A)) - self.b
            feasibility[idx] = all(constraint_values <= 0)
            constraint_violation[idx] = sum([x if x > 0 else 0 for x in constraint_values])
        return feasibility, constraint_violation

    def calculate_constraint_value(self, chromosome):
        return np.matmul(chromosome, np.transpose(self.A))
