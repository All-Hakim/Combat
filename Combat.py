import time
class Combat:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
    def demarrerCombat(self):
        print("Le combat va commencer ! Preparez-vous a en decoudre !")
        time.sleep(1)
        
        print(f"{self.joueur1.getNom()} affronte {self.joueur2.getNom()} ! Que le meilleur gagne !")
        time.sleep(1)
        print('Preparation des joueurs ...')
        print('...............................................................')
        time.sleep(1)
        while self.joueur1.getVie()>0 and self.joueur2.getVie()>0:
            if self.joueur1.tour == 'joueur1':
                self.joueur1.attaque(self.joueur2)
                self.joueur1.tour = 'joueur2'
                print('...............................................................')
                time.sleep(0.75)
                
            else:
                self.joueur2.attaque(self.joueur1)
                self.joueur1.tour ='joueur1'
                print('...............................................................')

                time.sleep(0.75)
        
        if self.joueur1.getVie()<=0:
            print (f'{self.joueur1.getNom()} est vaincu!!! c\'est {self.joueur2.getNom()} qui gagne le combat!!!')
        else:
            print (f'{self.joueur2.getNom()} est vaincu!!! c\'est {self.joueur1.getNom()} qui gagne le combat!!!')