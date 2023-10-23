# Créé par Lola, le 04/10/2023 en Python 3.7

import pygame
from pygame.locals import *
pygame.init()

#Constantes
n = 20
titre_fenetre = "Chaud Devant, Froid Derrière !"
largeur = 30 * n
hauteur = 30 * n
taille = hauteur // n
menu = "Images/welcome.png"
blue = (209,215,255)
white = (255,255,255)


def creation_fenetre(largeur,hauteur):
    """ création d'une fenêtre de taille largeur x hauteur"""
    global fenetre
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption(titre_fenetre)
    menu_background = pygame.image.load(menu).convert()
    pygame.transform.scale(menu_background, (largeur,hauteur))
    fenetre.blit(menu_background, (0,0))
    pygame.display.flip()

    running = True  # Variable pour contrôler la boucle principale
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False  # Quitter la boucle principale si l'utilisateur ferme la fenêtre
            if event.type == MOUSEBUTTONDOWN and event.button == 1:  # Vérifier le clic de souris
                # Récupérer les coordonnées du clic
                x, y = event.pos
                x2, y2 = event.pos
                # Vérifier si le clic est dans la zone du texte "Quitter"
                if (largeur // 2.3 <= x <= largeur // 2.3 + 200) and (hauteur // 1.4 <= y <= hauteur // 1.4 + 50):
                    running = False  # Quitter la boucle principale si l'utilisateur a cliqué sur "Quitter"
                # Vérifier si le clic est dans la zone du texte "Jouer"
                if (largeur // 2.34 <= x2 <= largeur // 2.34 + 200) and (hauteur // 1.6 <= y <= hauteur // 1.6 + 50):
                    running = False
                    import choisir_niveau #Importation du jeu lorsque la souris clique sur la zone de texte 'Jouer'


creation_fenetre(largeur, hauteur)
pygame.quit()

