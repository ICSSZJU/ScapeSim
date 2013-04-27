# -*- coding: utf-8 -*-
"""
This work is licensed under the Creative Commons 
Attribution-NonCommercial-ShareAlike 3.0 Unported 
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/3.0/.


Programming:Zhang Hong
"""

class PD(object):
    def __init__(self,R,S,T,P):
        assert T>R>P>S,"must satisfy condition:T>R>P>S"
        self.game_matrix={("c","c"):(R,R),("c","d"):(S,T),("d","c"):(T,S),("d","d"):(P,P)}
        
    def do(self,left,right):
        return self.game_matrix[(left.strategy,right.strategy)]
        