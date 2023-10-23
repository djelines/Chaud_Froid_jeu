# Créé par Lola, le 10/10/2023 en Python 3.7

import pygame
from pygame.locals import *
pygame.init()

#Constantes
n = 20
titre_fenetre = "Chaud Devant, Froid Derrière !"
largeur = 30 * n
hauteur = 30 * n
taille = hauteur // n
fond = "Images/niveau2.png"


def creation_fenetre(largeur,hauteur):
    """ création d'une fenêtre de taille largeur x hauteur"""
    global fenetre
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption(titre_fenetre)
    fond_niveau = pygame.image.load(fond).convert()
    pygame.transform.scale(fond_niveau, (largeur,hauteur))
    fenetre.blit(fond_niveau, (0,0))
    pygame.display.flip()


    running = True  #Variable pour contrôler la boucle principale
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False  #Quitter la boucle principale si l'utilisateur ferme la fenêtre
            if event.type == MOUSEBUTTONDOWN and event.button == 1:  #Vérifier le clic de souris
                #Récupérer les coordonnées du clic
                x, y = event.pos
                x2, y2 = event.pos
                x3, y3 = event.pos
                x4, y4 = event.pos
                #Vérifier si le clic est dans la zone du texte "Niveau Impossible"
                if (largeur // 2.3 <= x <= largeur // 2.3 + 200) and (hauteur // 1.4 <= y <= hauteur // 1.4 + 50):
                    running = False
                    import jeu_niv_impossible  #Importation du jeu de niveau impossible lorsque la souris clique sur la zone de texte 'Niveau Impossible'
                #Vérifier si le clic est dans la zone du texte "Niveau 3"
                if (largeur // 2.34 <= x2 <= largeur // 2.34 + 200) and (hauteur // 1.6 <= y2 <= hauteur // 1.6 + 50):
                    running = False
                    import jeu_niv3 #Importation du jeu de niveau 3 lorsque la souris clique sur la zone de texte 'Niveau 3'
                if (largeur // 2.34 <= x3 <= largeur // 2.34 + 200) and (hauteur // 2.0 <= y3 <= hauteur // 2.0 + 50):
                    running = False
                    import jeu_niv2 #Importation du jeu de niveau 2 lorsque la souris clique sur la zone de texte 'Niveau 2'
                if (largeur // 2.34 <= x4 <= largeur // 2.34 + 200) and (hauteur // 2.5 <= y4 <= hauteur // 2.5 + 50):
                    running = False
                    import jeu_niv1 #Importation du jeu de niveau 1 lorsque la souris clique sur la zone de texte 'Niveau 1'



creation_fenetre(largeur,hauteur)
pygame.quit()