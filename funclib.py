# -*- coding: utf-8 -*-
"""
This work is licensed under the Creative Commons 
Attribution-NonCommercial-ShareAlike 3.0 Unported 
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/3.0/.


Programming:Zhang Hong
"""

import math

class fermi(object):
    def __init__(self,beta):
        self.beta=beta
    
    def __call__(self,left,right):
        try:
            return 1.0/(1+math.exp(self.beta*(left.payoff-right.payoff)))
        except:
            if left.payoff-right.payoff>(700.0/self.beta):
                return 0.0
            elif right.payoff-left.payoff>(700.0/self.beta):
                return 1.0
            
    
