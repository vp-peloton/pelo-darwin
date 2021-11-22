#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 08:38:06 2017

@author: vijaypappu
"""

import random
import numpy as np


class ConstrainedGARunner(object):
    def __init__(self, ga_orchestrator):
        self.ga_orchestrator = ga_orchestrator

    def run(self):
        population = self.ga_orchestrator.generate_population() # nothing changes here
        feasibility, constraint_violation = self.ga_orchestrator.evaluate_feasibility(population)
        objective_values = self.ga_orchestrator.evaluate_objective(population)
        generation = 0
        while generation < self.ga_orchestrator.generations:
            print("No of feasible solutions at generation {}: {}".format(generation, sum(feasibility)))
            generation = generation + 1
            population = self.next_generation(population, objective_values,
                                              feasibility, constraint_violation)
            feasibility, constraint_violation = self.ga_orchestrator.evaluate_feasibility(population)
            objective_values = self.ga_orchestrator.evaluate_objective(population)
        
        count = 0
        for a,b in zip(feasibility, constraint_violation):
            print(count, str(a), str(b))
            count = count + 1
        feasible_solutions = feasibility == True
        feasible_population = population[feasible_solutions]
        feasible_objective_values = objective_values[feasible_solutions]
        print(np.where(feasible_solutions))
        # solution_indices = feasible_objective_values == max(object ive_values[feasible_solutions])
#         for idx in np.where(solution_indices)[0]:
        # for idx in np.where(feasible_solutions)[0]:
        for idx, chromosome in enumerate(feasible_population):
            chromosome = feasible_population[idx]
            constraint_value = self.ga_orchestrator.calculate_constraint_value(chromosome)
            print(str(feasible_objective_values[idx]) + ","  + str(constraint_value))
        
        return population

    def next_generation(self, population, objective_values, 
                        feasibility, constraint_violation):
        size = len(objective_values)
        nexts = []
        while len(nexts) < size:
            parents_indices = self.ga_orchestrator.select_parents(objective_values,
                                                                  feasibility,
                                                                  constraint_violation)  # tuple of integers - done
            parents = self.get_parents(population, parents_indices)  # array of bool arrays - done
            cross = random.random() < self.ga_orchestrator.probability_crossover()  # random number - done
            children = self.ga_orchestrator.create_offsprings(parents) if cross else parents  # array of bool arrays - done
            for ch in children:
                mutate = random.random() < self.ga_orchestrator.probability_mutation()
                nexts.append(self.ga_orchestrator.mutate(ch) if mutate else ch)  # array of bool array - done
        return np.array(nexts[0:size])

    def get_parents(self, population, indices):
        return population[np.array(indices)]