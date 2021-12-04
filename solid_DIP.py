"""Dependency Inversion Principle:The use of High Level Classes or high level modules should not depend directly tp low level modules instead they should depend on abstraction it means some sort of abstract class or abstract method so it will rather depend on interfaces than direct implentation so that way you can swap one for another with python we have duck typing stick one with the other with different class but same interface signature but it's better to have them separately"""
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3


class Person:
    def __init__(self, name):
        self.name = name

class Relationship_Browser:
    @abstractmethod
    def find_all_children_of(self,name):pass
class Relationships(Relationship_Browser):
    def __init__(self):
        self.relations = []

    def add_parent_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )
    def find_all_children_of(self,name):
        for r in self.relations:
            if r[0]==name and r[1]==Relationship.PARENT:
                yield r[2].name   
  
class Research:
    def __init__(self,browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}') 
    # def __init__(self,relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name =='John'and r[1]==Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}')
    
       