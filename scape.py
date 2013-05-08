# -*- coding: utf-8 -*-
"""
This work is licensed under the Creative Commons 
Attribution-NonCommercial-ShareAlike 3.0 Unported 
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/3.0/.

Programming:Zhang Hong
"""

import random
import networkx as nx
import numpy as np

class scape(object):
    netdict={"grid":nx.grid_2d_graph,"ring":nx.cycle_graph,"random graph":nx.gnm_random_graph,"regular graph":nx.random_regular_graph} 

    def __init__(self,type,*para,**namepara):
        self.land=scape.netdict[type](*para)
        self.type=type
    
    def __getitem__(self,coordinate):
        return self.land.node[coordinate]["agent"]
        
    @property
    def capacity(self):
        return len(self.land)
        
    def add_agents(self,agents):
        self.agents=agents
        diff=self.capacity-len(self.agents)
        if diff:
            agents_plus_dummy=self.agents+[None]*diff
            random.shuffle(agents_plus_dummy)
        else:
            agents_plus_dummy=self.agents
        agent_dict=dict(zip(self.land.nodes(),agents_plus_dummy))
        nx.set_node_attributes(self.land,"agent",agent_dict)
        for agent in self.agents:
            agent.register_scape(self)
        self.init_coordinate()
        
    def add_agent(self,agent,coordinate):
        self.agents.append(agent)
        agent.register_scape(self)
        agent.coordinate=coordinate
        self.land.node[coordinate]["agent"]=agent
        
    def del_agent(self,agent):
        self.land.node[agent.coordinate]["agent"]=None
        del agent
        
    def add_link(self,left,right):
        self.land.add_edge(left.coordinate,right.coordinate)
        
    def cut_link(self,left,right):
        self.land.remove_edge(left.coordinate,right.coordinate)        
        
    def init_coordinate(self):
        for n in self.land.nodes(data=True):
            if n[1]["agent"] is not None:
                n[1]["agent"].coordinate=n[0]
            
    
    def move(self,agent,coordinate):
        assert agent.coordinate!=coordinate,"can't move to original coordinate"
        assert self.land.node[coordinate]["agent"]==None,"can't move to coordinate which is occupied"
        self.land.node[coordinate]["agent"]=agent
        self.land.node[agent.coordinate]["agent"]=None
        agent.coordinate=coordinate
    
    def neighbors_of(self,agent):
        return [self.land.node[neighbor]["agent"] for neighbor in self.land[agent.coordinate] if self.land.node[neighbor]["agent"] is not None]
            
    def neighbor_coordinates_of(self,agent):
        return [neighbor for neighbor in nx.all_neighbors(self.land,agent.coordinate)]  
    
    def non_occupied(self):
        return [node for node in self.land.nodes() if self[node]==None]
        
    def is_occupied(self,coordinate):
        return bool(self[coordinate])
        
    def __str__(self):
        return "scape:type="+str(self.type)+",capacity="+str(self.capacity)
        
    def __repr__(self):
        return self.__str__()
        
            



        
