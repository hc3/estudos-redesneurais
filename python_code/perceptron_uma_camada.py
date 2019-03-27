#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:15:16 2019

@author: hc3
"""

import numpy as np

entradas = np.array([5, 7, 5])
pesos = np.array([0.8, 0.1, 0])

def soma(e ,p):
    return e.dot(p)

s = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

r = stepFunction(s)