# -*- coding: utf-8 -*-
"""
This work is licensed under the Creative Commons 
Attribution-NonCommercial-ShareAlike 3.0 Unported 
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/3.0/.

Programming:Zhang Hong
"""

import random
import copy
import funclib

class agent(object):
    def __init__(self,strategy):
        self.strategy=strategy
        
    def register_scape(self,scape):
        self.scape=scape
    
    @property    
    def neighbor_coordinates(self):
        return self.scape.neighbor_coordinates_of(self)
        
    @property
    def non_agent_neighbors(self):
        neighbor_coor=self.neighbor_coordinates
        for n in self.neighbors:
            neighbor_coor.remove(n.coordinate)
        return neighbor_coor
    
    @property
    def has_neighbor(self):
        return bool(len(self.neighbors))
        
    @property
    def neighbors(self):
        return self.scape.neighbors_of(self)      
        
    def move_to(self,coordinate):
        self.scape.move(self,coordinate)
    
    def reproduce(self,coordinate):
        new_agent=copy.copy(self)
        self.scape.add_agent(new_agent,coordinate)
        
    def imitate(self,right):
        self.strategy=right.strategy
        
    def imitate_by_func(self,right,func=funclib.fermi(1)):
        if random.random()<func(self,right):
            self.imitate(right)
        
    def cut_link_with(self,right):
        self.scape.cut_link(self,right)
    
    def add_link_with(self,right):
        self.scape.add_link(self,right)
        
    def die(self):
        self.scape.del_agent(self)
        
    def __str__(self):
        return "agent:"+"strategy="+str(self.strategy)+" coordinate="+str(self.coordinate)
        
    def __repr__(self):
        return self.__str__()
        
def agent_generator(participants):
    assert isinstance(participants,dict)
    plist=[[agent(key) for i in range(value)] for key,value in participants.items()]
    agents=[]
    for a in plist:
        agents+=a
    random.shuffle(agents)
    return agents
    
