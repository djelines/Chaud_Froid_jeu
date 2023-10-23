
# Biblio
from random import *
import pygame
from pygame.locals import *


pygame.init()


# Nos constantes
n = 20  # nbr de cases par ligne et colonne
titre_fenetre = "Chaud Devant, Froid Derrière !"
largeur = 30 * n
hauteur = 30 * n
taille = hauteur // n

# Couleurs

yellow = (255, 255, 204)


# Plateau_de_Jeu
Blanc = "Images/Blanc.png"
Gris = "Images/Gris.png"
Noir = "Images/Noir.png"
Bleu = "Images/Bleu1.png"
Bleu_2 = "Images/Bleu2.png"
Vert = "Images/Vert1.png"
Vert_2 = "Images/Vert2.png"
Orange = "Images/Orange1.png"
Orange_2 = "Images/Orange2.png"
Rouge = "Images/Rouge1.png"
Rouge_2 = "Images/Rouge2.png"
Jaune = "Images/Jaune1.png"
Jaune_2 = "Images/Jaune2.png"


def creation_fenetre(largeur, hauteur):
    """ création d'une fenêtre de taille largeurxhauteur avec le titre de la fenetre"""
    global fenetre
    # Design de la fenêtre Pygame
    fenetre = pygame.display.set_mode((largeur, hauteur))
    #  Titre
    pygame.display.set_caption(titre_fenetre)


def musique():
    """ création de la fonction musique """
    #Importation de la musique
    pygame.mixer.music.load('Song/8bits.mp3')
    #gestion du son
    pygame.mixer.music.set_volume(0.6)
    #gestion de la boucle de la musique
    pygame.mixer.music.play(-1)


def affiche_all():
    """ Affiche tous les éléments de la fenetre de jeu """
    # Texte du jeu
    font = pygame.font.SysFont('comicsansms,lucidasans,Arial', 17)
    texte = font.render('Chaud Devant, Froid Derrière !', True, yellow)
    fenetre.blit(texte, (largeur // 3.3, hauteur // 500))
    pygame.display.flip()


def placer_sprite_rouge_aleatoire(n):
    ligne = randint(0, n - 2)
    colonne = randint(0, n - 2)
    return ligne+1, colonne+1


def plateau(largeur, hauteur, n):
    """ création du plateau avec n colonnes et n lignes """
    for ligne in range(1, n):
        for colonne in range(n):
            # Calculer les coordonnées de la case
            x = colonne * taille
            y = ligne * taille
            # Dessiner la case
            blanc = pygame.image.load(Blanc).convert()
            blanc = pygame.transform.scale(blanc, (taille, taille))
            fenetre.blit(blanc, (x, y))
    pygame.display.flip()

# Générer les coordonnées aléatoires une fois
ligne_rouge, colonne_rouge = placer_sprite_rouge_aleatoire(n)

def affiche_solution():
    # Placer le sprite Rouge2 aux coordonnées générées
    sprite_rouge = pygame.image.load(Rouge_2).convert()
    sprite_rouge = pygame.transform.scale(sprite_rouge, (taille, taille))
    x_rouge = colonne_rouge * taille
    y_rouge = ligne_rouge * taille + 1
    fenetre.blit(sprite_rouge, (x_rouge, y_rouge))

    pygame.image.save(fenetre, "Images/plateau.jpg")
    #pygame.display.flip() # POUR AFFICHER LA SOLUTION

def recouvrir(L):
    for j in range(1,len(L)):
            for i in range(len(L[j])):
                if L[j][i] == "-":
                    gris = pygame.image.load(Gris).convert()
                    gris = pygame.transform.scale(gris, (taille, taille))
                    fenetre.blit(gris, (i * taille, j * taille))
    pygame.display.flip()


def affichage(L):
    for ligne in L:
        for val in ligne:
            print(f'{val:1}', end="\t")
        print("")

def fond_plateau_solution():
    fond = pygame.image.load("Images/plateau.jpg").convert()
    fenetre.blit(fond,(0,0))

def YouWin():
    fond = pygame.image.load("Images/winner2.png").convert()
    fenetre.blit(fond, (0, 0))
    pygame.display.flip()
    pygame.time.wait(1000)


def attente_clic():
    """
    attente d'un clic et qui retourne les coordonnées du clic
    ou mets fin au jeu
    """
    L = [['-' for i in range(1,n+1)] for i in range(20)]
    compteur = 0
    running = True  # Variable pour contrôler la boucle principale

    while running and compteur<1:

        for event in pygame.event.get():

            if event.type == QUIT:
                running = False  # Quitter la boucle principale si l'utilisateur ferme la fenêtre

            if event.type == MOUSEBUTTONDOWN :
                if event.button == 1:

                    clic_x = event.pos[0]
                    clic_y = event.pos[1]
                    colonne = clic_x // taille
                    ligne = clic_y // taille
                    coord_clic_souris = (ligne, colonne)
                    print("coordonnées clic souris :", coord_clic_souris)
                    L[ligne][colonne] = 'x'
                    affichage(L)
                    if ligne == ligne_rouge and colonne == colonne_rouge:
                        print("BRAVO VOUS ETES TROP FORT !!!")
                        affiche_solution()
                        YouWin()
                        running=False

                    else:
                        print("essaie encore")
                        compteur+=1
                        print("compteur :", compteur)


            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False  # Quitter la boucle principale lorsque la touche Échap est pressée

        font = pygame.font.SysFont('comicsansms,lucidasans,Arial', 17)
        texte_2 = font.render(f'Compteur : {compteur}', True, yellow)
        fenetre.blit(texte_2, (largeur // 15, hauteur // 500))
        pygame.display.flip()
        fond_plateau_solution()
        recouvrir(L)
        pygame.display.flip()
  # Quitter pygame
    pygame.quit()


# MAIN

creation_fenetre(largeur, hauteur)
affiche_all()
musique()
plateau(largeur, hauteur, n)
affiche_solution()
fond_plateau_solution()
attente_clic()
pygame.quit()




