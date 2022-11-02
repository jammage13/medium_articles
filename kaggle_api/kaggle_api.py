#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 19:47:13 2022

@author: jam
"""

import kaggle

api = kaggle.api

api.dataset_list(search='titanic')
api.dataset_list()

api.competitions_list()
api.competition_download_files('titanic')

api.competitions_data_list_files('titanic')

api.competitions_data_list_files_with_http_info('titanic')

api.dataset_download_file('titanic/data//itanic/train.csv', 'train.csv')
api.dataset_download_files('titanic/data')
