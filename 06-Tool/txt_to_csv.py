# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 20:42:42 2019

@author: ASUS
"""

import numpy as np  
import pandas as pd  
  
txt = np.loadtxt('USAir97.txt')  
txtDF = pd.DataFrame(txt)  
txtDF.to_csv('USAir97.csv',index=False)