#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 22:51:36 2017

@author: vijaypappu
"""
from .linear_inequality_constraint import LinearInequalityConstraint
import numpy as np

class FactoryConstraint(object):

    @staticmethod
    def init(config):
        operator = config["operator"]
        if(operator == "linear_inequality"):
            A_path = config["A"]
            b = np.array([config["b"]])
            f = open(A_path, 'r')
            x = [float(x) for x in f.read().split("\n")]
            print(x)
            A = np.array(x)
            return LinearInequalityConstraint(A, b)
        else:
            raise Exception("Invalid constraint operator!")