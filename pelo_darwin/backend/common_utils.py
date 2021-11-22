#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:52:45 2017

@author: vijaypappu
"""

from numpy import array, squeeze
from scipy.sparse import csc_matrix
import json


class CommonUtils(object):
    @staticmethod
    def load_json(json_path):
        with open(json_path) as f:
            config = json.load(f)
        return config

    @staticmethod
    def find_rank(int_list, value):

        int_list = sorted(int_list)
        if(value < min(int_list) or value > max(int_list)):
            raise Exception('The value is not in range!')

        left = 0
        right = len(int_list) - 1
        # middle = get_middle(left, right)
        middle = (left + right) // 2
        while (left < right):
            mid_value = int_list[middle]
            if(value == mid_value):
                return middle + 1
            elif(value < mid_value):
                right = middle
                # middle = get_middle(left, right)
                middle = (left + right) // 2
                if((right - left) == 1):
                    return right + 1
            else:
                left = middle
                # middle = get_middle(left, right)
                middle = (left + right) // 2
                if((right - left) == 1):
                    return right + 1

    @staticmethod
    def get_middle(m, n):
        return ((m + n) // 2)

    @staticmethod
    def convert_to_boolean(chromosome):
        return array(squeeze(chromosome.toarray()), dtype=bool)
        
    @staticmethod
    def convert_from_boolean(bool_array):
        return csc_matrix(bool_array, dtype=int)
