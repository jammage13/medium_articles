# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:58:28 2022

@author: Jam
"""

import random
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=50000,
                           n_classes=2,
                           n_features=30,
                           weights=[0.95, 0.5])

def random_undersample(X, y, ratio):
    n_rows = len(y)
    n_minority = sum(y==1)
    n_majority = n_rows - n_minority
    n_sample = 