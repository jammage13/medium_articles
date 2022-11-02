#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 19:47:13 2022

@author: jam
"""

import kaggle
import zipfile
import os

api = kaggle.api

api.competitions_list()

api.competitions_list(search='titanic')

api.competitions_data_list_files('titanic')

api.competition_download_files('titanic')

with zipfile.ZipFile('titanic.zip', 'r') as zip_ref:
    zip_ref.extractall('C:/Users/Jam/Documents/Python Scripts/Medium/medium_articles/kaggle_api')
    
os.listdir()

