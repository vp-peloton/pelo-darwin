#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 10:49:55 2017

@author: vijaypappu
"""

from .rank_selection import RankSelection
from .roulette_wheel_selection import RouletteWheelSelection
from .tournament_selection import TournamentSelection
from .constrained_tournament_selection import ConstrainedTournamentSelection


class FactoryParents(object):

    @staticmethod
    def init(config):

        operator = config["operator"]

        if(operator == "rank"):
            return RankSelection()

        elif(operator == "roulette"):
            return RouletteWheelSelection(config)

        elif(operator == "tournament"):
            return TournamentSelection(config)
        
        elif(operator == "constrained_tournament"):
            return ConstrainedTournamentSelection(config)        

        else:
            raise Exception("Invalid parents operator!")
