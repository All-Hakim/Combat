from abc import ABC, abstractmethod

class Personnage(ABC):
    def __init__(self,nom) :
        self.__nom = nom
        self.__vie = 100
        self.__force = 0
        self.__experience = 0
        self.__degats = 0
        self.tour = 'joueur1'
    def frappe(self, cible,forceFrappe):
        forceFrappe = self.__force
        cible.__vie -= forceFrappe

    def esquive():
        pass
    
    def recoitDegat(self, adverse):
        self.__degats += adverse.__force
    
    def getNom(self):
        return self.__nom
    
    def setNom(self,nom):
        self.__nom = nom
        
    def getVie(self):
        return self.__vie
    def setVie(self, vie):
        self.__vie = vie
        
    def getForce(self):
        return self.__force
    def setForce(self,force):
        self.__force = force
        
    def getExperience(self):
        return self.__experience

    def setExperience(self,experience):
        self.__experience = experience
    
    def getDegats(self):
        return self.__degats
    def setDegats(self,degats):
        self.__degats = degats
        





