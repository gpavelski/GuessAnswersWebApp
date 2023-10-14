# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 16:00:50 2023

@author: Guilherme
"""

import os

class Config:  
   SECRET_KEY = os.environ.get('SECRET_KEY')
   # ... other configurations ...  
