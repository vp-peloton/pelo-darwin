#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 10:46:45 2017

@author: vijaypappu
"""

from .balance_mutator import BalanceMutator


class FactoryMutator(object):

    @staticmethod
    def init(config):

        operator = config["operator"]

        if(operator == "balance"):
            return BalanceMutator()

        else:
            raise Exception("Invalid mutator operator!")
