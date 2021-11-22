#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 12:19:17 2017

@author: vijaypappu
"""

import random
import numpy as np


class GARunner(object):
    def __init__(self, ga_orchestrator):
        self.ga_orchestrator = ga_orchestrator

    def run(self):
        population = self.ga_orchestrator.generate_population()  # done
        generation = 0
        while generation < self.ga_orchestrator.generations:
            fitness_values = self.ga_orchestrator.evaluate_fitness(population)  # array - done
            population = self.next_generation(population, fitness_values)  # array of bool arrays - done
            generation = generation + 1
        fitness_values = self.ga_orchestrator.evaluate_fitness(population)
        for x,y in zip(population, fitness_values):
            print(x, y)
        return population

    def next_generation(self, population, fitness_values):
        size = len(fitness_values)
        nexts = []
        while len(nexts) < size:
            parents_indices = self.ga_orchestrator.select_parents(fitness_values)  # tuple of integers - done
            parents = self.get_parents(population, parents_indices)  # array of bool arrays - done
            cross = random.random() < self.ga_orchestrator.probability_crossover()  # random number - done
            children = self.ga_orchestrator.create_offsprings(parents) if cross else parents  # array of bool arrays - done
            for ch in children:
                mutate = random.random() < self.ga_orchestrator.probability_mutation()
                nexts.append(self.ga_orchestrator.mutate(ch) if mutate else ch)  # array of bool array - done
        return np.array(nexts[0:size])

    def get_parents(self, population, indices):
        return population[np.array(indices)]
