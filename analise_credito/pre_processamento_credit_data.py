# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:13:04 2020

@author: alexp
"""

import pandas as pd
base = pd.read_csv('credit-data.csv')
base.describe()