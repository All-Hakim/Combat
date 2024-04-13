import random
import time
from Personnage import Personnage
class RoiSorcier(Personnage):
    FORCE_FRAPPE_1 = 5
    FORCE_FRAPPE_2 = 20
    
    def __init__(self,nom) :
        super().__init__(nom)
    def frappeAvecSonEpee(self, adverse):
        self.setForce(self.FORCE_FRAPPE_1+self.getExperience())
        self.frappe(adverse,self.getForce())
        self.setExperience(self.getExperience()+1)
        adverse.recoitDegat(self)
        if adverse.getVie()<0:
            adverse.setVie(0)
        time.sleep(0.5)
        print(f'{self.getNom() } attaque avec son epee {adverse.getNom()} ({self.getForce()} points de degats) (+1 aux prochaines frappes!!)')
        time.sleep(0.5)
        print(f'{self.getNom() }: PV = {self.getVie()};         Total de degats subis : {self.getDegats()};         XP:{self.getExperience()}')
        time.sleep(0.5)
        print(f'{adverse.getNom()}: PV = {adverse.getVie()};         Total de degats subis : {adverse.getDegats()};         XP:{adverse.getExperience()}')

    def attaqueAvecSonNazgul(self,adverse):
        self.setForce(self.FORCE_FRAPPE_2+self.getExperience())
        self.frappe(adverse,self.getForce())
        self.setExperience(self.getExperience()+1)
        adverse.recoitDegat(self)
        if adverse.getVie()<0:
            adverse.setVie(0)
            
        time.sleep(0.5)
        print(f'{self.getNom() } attaque avec son Nazgul {adverse.getNom()} ({self.getForce()} points de degats) (+1 aux prochaines frappes!!)')
        time.sleep(0.5)
        print(f'{self.getNom() }: PV = {self.getVie()};         Total de degats subis : {self.getDegats()};         XP:{self.getExperience()}')
        time.sleep(0.5)
        print(f'{adverse.getNom()}: PV = {adverse.getVie()};         Total de degats subis : {adverse.getDegats()};         XP:{adverse.getExperience()}')
    
    def attaque(self, adverse):
        def random_choice():
            return random.choice([1, 2])
        if random_choice() == 1:
            self.frappeAvecSonEpee(adverse)
        else:
            self.attaqueAvecSonNazgul(adverse)
        

























