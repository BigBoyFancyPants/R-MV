# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 14:43:30 2022

@author: Timothy
"""

class Engineers:
    skill = "Problem solver"
    def __init__(self,name,_type,years_of_experience):
        self.name = name
        self._type = _type
        self.years_of_experience = years_of_experience
    
    
eng1 = Engineers("Jeff", "ELE", "25")
eng2 = Engineers("Ben","MEC","5")
print(eng1.skill+" "+eng1.name+" "+eng1._type+" "+eng1.years_of_experience)
print(eng2.skill+" "+eng2.name+" "+eng2._type+" "+eng2.years_of_experience)

print("yhtomiT")
for i in range(0,3**2+1):# number was to big so picked my second favourite
    print(i)
    