# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:24:24 2013

@author: zhang
"""

import math
from decimal import *

class fermi(object):
    def __init__(self,beta):
        self.beta=beta
    
    def __call__(self,left,right):
        if left.payoff-right.payoff>(700.0/self.beta):
            return 0.0
        elif right.payoff-left.payoff>(700.0/self.beta):
            return 1.0
        else:
            return 1.0/(1+math.exp(self.beta*(left.payoff-right.payoff)))

    
