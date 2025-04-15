"""
Programme réalisé par nom, prénom, classe
"""
import pygame
from random import randint
import random

# variables du niveau
NB_TILES = 666   # nombre de tiles à charger
TITLE_SIZE = 32  # définition du dessin (carré)
largeur = 26      # largeur du niveau
hauteur = 18      # hauteur du niveau
tiles = []       # liste d'images tiles
clock = pygame.time.Clock()

# définition du niveau
niveau = [[47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 73, 73, 73, 73, 73],
          [47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 73],
          [47, 47, 170, 189, 189, 171, 47, 170, 189, 171, 47, 170, 189, 189, 171, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 73],
          [47, 47, 187, 47, 47, 187, 47, 187, 47, 187, 47, 187, 47, 47, 142, 189, 189, 189, 189, 189, 189, 47, 47, 47, 47, 73],
          [47, 47, 187, 47, 47, 187, 47, 187, 47, 187, 47, 187, 47, 47, 187, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 73],
          [47, 47, 187, 47, 47, 193, 189, 194, 47, 193, 189, 194, 47, 47, 187, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
          [47, 47, 187, 47, 47, 47, 70, 70, 70, 70, 70, 47, 47, 47, 187, 47, 47, 47, 47, 516, 569, 569, 569, 569, 569, 569],
          [47, 47, 187, 47, 47, 48, 72, 73, 74, 73, 72, 46, 47, 47, 187, 47, 47, 47, 47, 547, 486, 496, 496, 486, 486, 496],
          [47, 47, 187, 47, 47, 48, 73, 118, 119, 120, 73, 46, 47, 47, 187, 47, 47, 47, 47, 547, 496, 486, 486, 496, 486, 486],
          [47, 47, 187, 47, 47, 48, 74, 141, 142, 142, 142, 189, 189, 189, 166, 47, 47, 47, 47, 547, 496, 486, 486, 496, 486, 496],
          [47, 170, 166, 47, 47, 48, 73, 164, 142, 166, 73, 46, 47, 47, 47, 47, 47, 47, 47, 547, 486, 496, 486, 496, 486, 486],
          [47, 187, 47, 47, 47, 48, 72, 74, 142, 74, 72, 46, 47, 47, 47, 47, 47, 47, 118, 565, 444, 454, 444, 454, 444, 455],
          [47, 187, 47, 118, 569, 569, 507, 511, 142, 587, 517, 517, 517, 517, 517, 517, 517, 517, 521, 168, 168, 168, 168, 168, 168, 468],
          [47, 187, 47, 215, 496, 496, 496, 534, 142, 532, 496, 496, 496, 496, 496, 496, 496, 496, 534, 168, 168, 168, 168, 168, 168, 468],
          [47, 187, 47, 215, 496, 496, 496, 534, 142, 532, 496, 496, 496, 496, 496, 496, 496, 496, 534, 168, 168, 168, 168, 168, 168, 468],
          [47, 187, 47, 215, 496, 496, 496, 534, 142, 532, 496, 496, 496, 496, 496, 496, 496, 496, 534, 168, 168, 168, 168, 168, 168, 468],
          [47, 187, 47, 215, 496, 496, 496, 489, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 511, 168, 167, 168, 168, 168, 169, 468],
          [47, 187, 47, 215, 496, 496, 496, 496, 496, 496, 496, 496, 496, 496, 496, 496, 496, 496, 489, 490, 500, 490, 500, 490, 500, 501]]


decor = [[186, 184, 186, 229, 186, 185, 186, 185, 186, 185, 186, 185, 186, 0, 0, 0, 0, 157, 159, 160, 0, 0, 0, 0, 0, 0,],
         [207, 185, 226, 251, 185, 186, 185, 186, 185, 186, 185, 186, 185, 0, 0, 0, 0, 178, 177, 178, 0, 0, 0, 0, 0, 0,],
         [185, 185, 0, 0, 0, 0, 186, 0, 0, 0, 186, 0, 0, 0, 0, 0, 0, 199, 201, 200, 0, 0, 208, 0, 0, 0,],
         [184, 228, 0, 161, 163, 0, 185, 0, 185, 0, 185, 0, 229, 0, 0, 0, 0, 0, 0, 0, 0, 208, 207, 208, 0, 0,],
         [185, 229, 0, 163, 161, 0, 186, 0, 186, 0, 186, 0, 229, 0, 0, 0, 0, 256, 0, 256, 0, 0, 208, 0, 0, 0,],
         [186, 229, 0, 161, 163, 0, 0, 0, 185, 0, 0, 0, 229, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
         [303, 229, 0, 0, 0, 226, 250, 250, 250, 250, 250, 250, 251, 140, 0, 254, 232, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
         [278, 279, 0, 278, 279, 229, 0, 0, 0, 0, 0, 0, 140, 163, 0, 0, 254, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
         [276, 277, 0, 276, 277, 229, 0, 0, 0, 0, 0, 0, 0, 0, 0, 232, 0, 232, 0, 0, 0, 0, 0, 0, 0, 0,],
         [299, 300, 0, 299, 300, 229, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
         [228, 0, 0, 226, 250, 251, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
         [256, 0, 226, 251, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
         [229, 0, 229, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 253, 235, 233, 253, 0, 233,],
         [229, 0, 229, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 235, 0, 0, 0, 0, 235,],
         [256, 0, 229, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 233, 0, 0, 0, 0, 253,],
         [229, 0, 229, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 253, 0, 0, 0, 0, 233,],
         [229, 0, 229, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 235,],
         [256, 0, 229, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 233, 235, 253, 233, 235, 253,]]


collisions = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1,],
         [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1,],
         [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1,],
         [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
         [1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
         [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
         [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,],
         [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,],
         [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,],
         [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,],
         [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
         [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1,],
         [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1,],
         [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,],
         [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1,],
         [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,]]


class Personnage(pygame.sprite.Sprite):
    def __init__(self, position, size, img, collisions):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.size = size
        self.collisions = collisions
        self.x, self.y = position
        self.rect.x = self.x * size
        self.rect.y = self.y * size
        self.vie = 10
        self.maxVie = 10
        self.xp = 0
        self.niveau = 1
        self.nom = "Personnage"  # Nom par défaut

    def testCollisionsDecor(self, x, y):
        if self.collisions[self.y + y][self.x + x] == 0:
            self.x += x
            self.y += y

    def droite(self):
        self.testCollisionsDecor(1, 0)
        self.rect.x = self.x * self.size

    def gauche(self):
        self.testCollisionsDecor(-1, 0)
        self.rect.x = self.x * self.size

    def haut(self):
        self.testCollisionsDecor(0, -1)
        self.rect.y = self.y * self.size

    def bas(self):
        self.testCollisionsDecor(0, 1)
        self.rect.y = self.y * self.size

    def ajouterVie(self, vie):
        self.vie = min(self.vie + vie, self.maxVie)

    def retirerVie(self, vie):
        self.vie = max(self.vie - vie, 0)

    def monterExperience(self):
        self.xp += 2
        while self.xp >= 10:
            self.niveau += 1
            self.xp -= 10

    def estVivant(self):
        return self.vie > 0

    def decrire_combat(self, degats, adversaire):
        if degats >0:
            pass

class Combattant(Personnage):
    def __init__(self, position, size, img, collisions):
        super().__init__(position, size, img, collisions)
        self.force = 5

    def augmenterForce(self):
        self.force += 1

class Tank(Personnage):
    def __init__(self, position, size, img, collisions):
        super().__init__(position, size, img, collisions)
        self.force = 5

    def augmenterForce(self):
        self.force += 1

    def combat(self, adversaire):
        if not adversaire.estVivant():
            return
        attaque = randint(1, 4)
        degats = max(0, attaque * self.niveau * self.force - adversaire.niveau)
        adversaire.retirerVie(degats)
        print(self.decrire_combat(degats, adversaire))
        self.xp += degats
        if not adversaire.estVivant():
            print(f"{adversaire.nom} s'effondre !")
            self.augmenterForce()

class Grue(Personnage):
    def __init__(self, position, size, img, collisions):
        super().__init__(position, size, img, collisions)
        self.force = 10
        self.phrases_victoire = [
            "Grue porte un coup dévastateur à {0}, infligeant {1} points de dégâts !",
            "Grue attaque violemment {0}, causant {1} points de dégâts !",
            "Grue frappe de plein fouet {0}, infligeant {1} points de dégâts !",
            "Grue écrase {0} sous un coup brutal, infligeant {1} points de dégâts !",
            "Grue met KO {0} avec un coup puissant, infligeant {1} points de dégâts !"
        ]
        self.a_gagne = False  # ça sert a éviter les répétitions

    def augmenterForce(self):
        self.force += 1

    def combat(self, adversaire):
        if not adversaire.estVivant():
            return
        attaque = randint(1, 4)
        degats = max(1, attaque * self.niveau * self.force - adversaire.niveau)
        adversaire.retirerVie(degats)
        print(self.decrire_combat(degats, adversaire))

        if not adversaire.estVivant() and not self.a_gagne:
            phrase = random.choice(self.phrases_victoire)
            print(phrase.format(adversaire.nom, degats))
            self.a_gagne = True

        if not self.estVivant() and not self.a_gagne:
            print(f"{self.nom} a perdu le combat.")

        self.xp += degats
        if not adversaire.estVivant():
            print(f"{adversaire.nom} s'effondre !")
            self.augmenterForce()

    def resetCombat(self):
        """Réinitialise l'état de victoire de Grue à chaque début de combat."""
        self.a_gagne = False

class Monstre(Personnage):
    def __init__(self, position, size, img, collisions):
        super().__init__(position, size, img, collisions)
        self.force = 5

    def augmenterForce(self):
        self.force += 1

    def combat(self, adversaire):
        if not adversaire.estVivant():
            return
        attaque = randint(1, 4)
        degats = max(0, attaque * self.niveau * self.force - adversaire.niveau)
        adversaire.retirerVie(degats)
        print(self.decrire_combat(degats, adversaire))
        self.xp += degats
        if not adversaire.estVivant():
            print(f"{adversaire.nom} s'effondre !")
            self.augmenterForce()

class Magicien(Personnage):
    def __init__(self, position, size, img, collisions, mana, manaMax):
        super().__init__(position, size, img, collisions)  # Appelle le constructeur de Personnage
        self.maxMana = manaMax
        self.mana = mana

    def augmenterMana(self):
        self.maxMana += 10

    def ajouterMana(self):
        self.mana = min(self.mana + 1, self.maxMana)

    def retirerMana(self, mana):
        self.mana = max(self.mana - mana, 0)

    def combat(self, adversaire):
        if not adversaire.estVivant():
            return
        attaque = randint(1, 4)
        degats = max(0, attaque * self.niveau * 2 - adversaire.niveau)
        if self.mana > 0:
            adversaire.retirerVie(degats)
            self.retirerMana(1)
            print(f"{self.nom} lance un sort, infligeant {degats} dégâts à {adversaire.nom}.")
        else:
            adversaire.retirerVie(degats // 2)
            print(f"{self.nom} attaque faiblement, n'ayant plus de mana. {adversaire.nom} subit {degats // 2} dégâts.")
        self.xp += degats
        if not adversaire.estVivant():
            print(f"{adversaire.nom} est vaincu !")
            self.augmenterMana()

# Remplacer les classes et objets de combat par leurs variantes avec narration.



# Configuration Pygame
pygame.init()
fenetre = pygame.display.set_mode((largeur * TITLE_SIZE, (hauteur + 1) * TITLE_SIZE))
pygame.display.set_caption("Dungeon")
font = pygame.font.Font('freesansbold.ttf', 20)

def chargetiles(tiles):
    for n in range(0, NB_TILES):
        tiles.append(pygame.image.load('data/'+str(n)+'.png')) #attention au chemin

def afficheNiveau(niveau):
    for y in range(hauteur):
        for x in range(largeur):
            fenetre.blit(tiles[niveau[y][x]], (x * TITLE_SIZE, y * TITLE_SIZE))
            if decor[y][x] > 0:
                fenetre.blit(tiles[decor[y][x]], (x * TITLE_SIZE, y * TITLE_SIZE))

def afficheStats(personnage, x, y):
    stats = font.render(f"{personnage.nom}: Vie={personnage.vie} XP={personnage.xp}", True, (255, 255, 255))
    fenetre.blit(stats, (x, y))

def afficheScore(score):
    """
    affiche le score
    """
    #exemple bidon
    #scoreAafficher = font.render(str(score), True, (0, 255, 0))
    #fenetre.blit(scoreAafficher,(120,250))
    pass


perso = Personnage([1,1],TITLE_SIZE,"data/1.png",collisions)
perso2 = Personnage([3,3],TITLE_SIZE,"data/2.png",collisions)
perso3 = Personnage([3,5],TITLE_SIZE,"data/3.png",collisions)
perso4 = Personnage([1,5],TITLE_SIZE,"data/4.png",collisions)
perso5 = Personnage([1,3],TITLE_SIZE,"data/5.png",collisions)


aventuriers = pygame.sprite.Group()
aventuriers.add(perso)


mechants = pygame.sprite.Group()
mechants.add(perso2)
mechants.add(perso3)
mechants.add(perso4)
mechants.add(perso5)

fenetre.fill((0,0,0))   #efface la fenetre
chargetiles(tiles)  #chargement des images

# Classes spécifiques déjà définies : Grue, Monstre, Tank, Combattant, Magicien

# Création des personnages
grue = Grue([1, 16], TITLE_SIZE, "data/1.png", collisions)
grue.nom = "Grue"

springtrap = Monstre([23, 15], TITLE_SIZE, "data/4.png", collisions)
springtrap.nom = "Springtrap"

grolux = Tank([2, 9], TITLE_SIZE, "data/5.png", collisions)
grolux.nom = "Grolux"

le_magicien = Magicien([8, 2], TITLE_SIZE, "data/2.png", collisions, 20, 30)
le_magicien.nom = "Le magicien"


el_primo = Combattant([8, 9], TITLE_SIZE, "data/3.png", collisions)
el_primo.nom = "El Primo"

# Groupes de sprites
aventuriers = pygame.sprite.Group()
aventuriers.add(grue)

mechants = pygame.sprite.Group()
mechants.add(springtrap, grolux, le_magicien, el_primo)

# Fonction de duel
def duel(combattant, mechant):
    while combattant.estVivant() and mechant.estVivant():
        combattant.combat(mechant)
        if mechant.estVivant():
            mechant.combat(combattant)
        print(f"{combattant.nom}: Vie={combattant.vie}, XP={combattant.xp}")
        print(f"{mechant.nom}: Vie={mechant.vie}, XP={mechant.xp}")

    if combattant.estVivant():
        print(f"{combattant.nom} a gagné le duel!")
    else:
        print(f"{mechant.nom} a gagné le duel!")

# Boucle principale du jeu
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                grue.haut()
            elif event.key == pygame.K_DOWN:
                grue.bas()
            elif event.key == pygame.K_RIGHT:
                grue.droite()
            elif event.key == pygame.K_LEFT:
                grue.gauche()

    for mechant in mechants:
        if pygame.sprite.collide_rect(grue, mechant):
            print(f"Combat entre {grue.nom} et {mechant.nom}")
            duel(grue, mechant)
            if not mechant.estVivant():
                mechants.remove(mechant)

    # Affichage
    fenetre.fill((0, 0, 0))
    afficheNiveau(niveau)
    aventuriers.update()
    aventuriers.draw(fenetre)
    mechants.update()
    mechants.draw(fenetre)
    pygame.display.update()

pygame.quit()
