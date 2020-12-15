# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 21:11:23 2020

@author: Roger
"""

import array
import random

import pandas as pd
import numpy as np

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
    
def loadData():
    data = pd.read_csv("distancias.csv")
    header = list(data.columns)
    distancias = np.array(data)
    return header, distancias


ciudades, distancias = loadData()
cantCiudades = len(ciudades)


creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode='i', fitness=creator.FitnessMin)

toolbox = base.Toolbox()


toolbox.register("indices", random.sample, range(cantCiudades), cantCiudades)

toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalCamino(individual):
    distanciaGen = distancias[individual[-1]][individual[0]]
    for gene1, gene2 in zip(individual[0:-1], individual[1:]):
        distanciaGen += distancias[gene1][gene2]
    
    return distanciaGen,

toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalCamino)

def main():
    random.seed(169)
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    
    iteraciones = 40
    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, iteraciones, stats=stats, halloffame=hof, verbose=True)
    
    return pop, stats, hof

if __name__ == "__main__":
    
    _,_, hof= main()
    data = hof[0]
    
    
    print("Hall of Fame:",data)
    print("Camino optimo: ", end = "\n\t")
    
    
    for i in data:
        print(ciudades[i], end = ", " if i != data[len(data)-1] else "\n")
        
    total = 0
    for i in range(len(data)-1):
        total+= distancias[data[i]][data[i+1]]
    total+= distancias[data[0]][data[len(data)-1]];
    print("Menor coste de recorido: ",total)