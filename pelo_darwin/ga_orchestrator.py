#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:04:09 2017

@author: vijaypappu
"""

from .parents.factory_parents import FactoryParents
from .crossover.factory_crossover import FactoryCrossover
from .mutator.factory_mutator import FactoryMutator
from .fitness.factory_fitness import FactoryFitness
from .initiator.factory_initiator import FactoryInitiator
from .constraint.factory_constraint import FactoryConstraint
from .objective.factory_objective import FactoryObjective
import numpy as np

class GAOrchestrator(object):

    def __init__(self, config):

        print(config)
        initiator_config = config["initial"]
        self.initiator = FactoryInitiator.init(initiator_config)

        parents_config = config["parents"]
        self.parents = FactoryParents.init(parents_config)

        crossover_config = config["crossover"]
        self.crossover = FactoryCrossover.init(crossover_config)

        mutator_config = config["mutation"]
        self.mutator = FactoryMutator.init(mutator_config)

        fitness_config = config["fitness"]
        self.fitness = FactoryFitness.init(fitness_config)
        
        objective_config = config["objective"]
        self.objective = FactoryObjective.init(objective_config)

        constraint_config = config["constraint"]
        self.constraint = FactoryConstraint.init(constraint_config)

        self.generations = config["generations"]
        self.prob_crossover = config["prob_crossover"]
        self.prob_mutation = config["prob_mutation"]

    def probability_crossover(self):
        return self.prob_crossover

    def probability_mutation(self):
        return self.prob_mutation

    def generate_population(self):
        return self.initiator.generate()

    def evaluate_fitness(self, population):
        return self.fitness.evaluate(population)

    def create_offsprings(self, parents):
        return self.crossover.offsprings(parents)

    def mutate(self, chromosome):
        return self.mutator.mutate(chromosome)

    def select_parents(self, objective_values, feasiblity = np.array([]), 
                       constraint_violation = np.array([])):
        return self.parents.generate(objective_values, 
                                     feasiblity,
                                     constraint_violation)
    
    def evaluate_feasibility(self, population):
        return self.constraint.evaluate_constraints(population)
    
    def evaluate_objective(self, population):
        return self.objective.evaluate(population)

    def calculate_constraint_value(self, chromosome):
        return self.constraint.calculate_constraint_value(chromosome)

    def check_stop(self, fits_populations):
        self.counter += 1
        if self.counter % 10 == 0:
            best_match = list(sorted(fits_populations))[-1][1]
            fits = [f for f, ch in fits_populations]
            best = max(fits)
            worst = min(fits)
            ave = sum(fits) / len(fits)
            print(
                "[G %3d] score=(%4d, %4d, %4d): %r" %
                (self.counter, best, ave, worst,
                 self.chromo2text(best_match)))
            pass
        return self.counter >= self.limit
