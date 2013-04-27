# -*- coding: utf-8 -*-
"""
This work is licensed under the Creative Commons 
Attribution-NonCommercial-ShareAlike 3.0 Unported 
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/3.0/.


Programming:Zhang Hong
"""
import random
import agent as agt
import numpy as np
import collections as clt
import copy

class population(object):
    rand_method={"uniform":np.random.uniform,"normal":np.random.normal,"def":lambda x:x}
    def __init__(self,agents,scape):
        self.strategy_enum=agents.keys()
        agents=agt.agent_generator(agents)
        self.scape=scape
        self.scape.add_agents(agents)
        self.agents=self.scape.agents
        
        
    @property
    def population_size(self):
        return len(self.agents)
        
    @property 
    def capacity(self):
        return self.scape.capacity
        
    def __str__(self):
        return "population in scape-"+str(self.scape.type)
        
    def __repr__(self):
        return self.__str__()
        
    def set_agent_attr(self,name,method,*para):
        for agent in self.agents:
            agent.__setattr__(name,population.rand_method[method](*para))
            
    def set_scape_attr(self,name,method,*para):
        self.scape.set_scape_attr(name,method,*para)
        
    def mutate(self,p):
        for agent in self.agents:
            temp_enum=copy.copy(self.strategy_enum)
            if np.random.uniform()<p:
                if len(temp_enum)>2:
                    agent.strategy=random.choice(temp_enum.remove(agent.strategy))
                else:
                    temp_enum.remove(agent.strategy)
                    agent.strategy=temp_enum[0]

    
    @property
    def agent_summary(self):
        strategy=[agent.strategy for agent in self.agents]
        return dict(clt.Counter(strategy))
            
