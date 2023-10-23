
# Biblio
from random import *
import pygame
from pygame.locals import *


pygame.init()


# Nos constantes
n = 5  # nbr de cases par ligne et colonne
titre_fenetre = "Chaud Devant, Froid Derrière !"
largeur = 110 * n
hauteur = 110 * n
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
    font = pygame.font.SysFont('comicsansms,lucidasans,Arial', 30)
    texte = font.render('Chaud Devant, Froid Derrière !', True, yellow)
    fenetre.blit(texte, (largeur // 6.6, hauteur // 20))
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

    # Placer le sprite Rouge1 autour du sprite Rouge2
    for direction in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        dx, dy = direction
        new_row = ligne_rouge + dy
        new_col = colonne_rouge + dx
        if 1 <= new_row < n and 0 <= new_col < n:
            sprite_rouge = pygame.image.load(Rouge).convert()
            sprite_rouge = pygame.transform.scale(sprite_rouge, (taille, taille))
            x_rouge = new_col * taille
            y_rouge = new_row * taille
            fenetre.blit(sprite_rouge, (x_rouge, y_rouge))
# Placer le sprite Orange2 autour du sprite Rouge
    for direction in [(0, -2), (0, 2), (-2, 0), (2, 0), (1, -2), (1, 2), (-2, 1), (2, 1), (-1, -2), (-1, 2), (-2, -1), (2, -1),(-2, -2), (-2, 2), (2, -2), (2, 2)]:
        dx, dy = direction
        new_row = ligne_rouge + dy
        new_col = colonne_rouge + dx
        if 1 <= new_row < n and 0 <= new_col < n:
            sprite_orange2 = pygame.image.load(Orange_2).convert()
            sprite_orange2 = pygame.transform.scale(sprite_orange2, (taille, taille))
            x_orange2 = new_col * taille
            y_orange2 = new_row * taille
            fenetre.blit(sprite_orange2, (x_orange2, y_orange2))


    # Placer le sprite Orange1 autour du sprite Rouge
    for direction in [(0, -3), (0, 3), (-3, 0), (3, 0), (2, -3), (2, 3), (-3, 2), (3, 2), (-2, -3), (-2, 3), (-3, -2), (3, -2), (3, -3), (3, 3), (-3, 3), (3, 3), (-3, -3), (-3, 3), (-3, -3), (3, -3), (1, -3), (1, 3), (-3, 1), (3, 1), (-1, -3), (-1, 3), (-3, -1), (3, -1), (-3, -3), (-3, 3), (3, -3), (3, 3)]:
        dx, dy = direction
        new_row = ligne_rouge + dy
        new_col = colonne_rouge + dx
        if 1 <= new_row < n and 0 <= new_col < n:
            sprite_orange1 = pygame.image.load(Orange).convert()
            sprite_orange1 = pygame.transform.scale(sprite_orange1, (taille, taille))
            x_orange1 = new_col * taille
            y_orange1 = new_row * taille
            fenetre.blit(sprite_orange1, (x_orange1, y_orange1))
# Placer le sprite Jaune2 autour du sprite Rouge
    for direction in [(0, -4), (0, 4), (-4, 0), (4, 0), (3, -4), (3, 4), (-4, 3), (4, 3), (-3, -4), (-3, 4), (-4, -3), (4, -3), (4, -4), (4, 4), (-4, 4), (4, 4), (-4, -4), (-4, 4), (-4, -4), (4, -4), (2, -4), (2, 4), (-4, 2), (4, 2), (-2, -4), (-2, 4), (-4, -2), (4, -2), (1, -4), (1, 4), (-4, 1), (4, 1), (-1, -4), (-1, 4), (-4, -1), (4, -1), (-4, -4), (-4, 4), (4, -4), (4, 4)]:
        dx, dy = direction
        new_row = ligne_rouge + dy
        new_col = colonne_rouge + dx
        if 1 <= new_row < n and 0 <= new_col < n:
            sprite_jaune2 = pygame.image.load(Jaune_2).convert()
            sprite_jaune2 = pygame.transform.scale(sprite_jaune2, (taille, taille))
            x_jaune2 = new_col * taille
            y_jaune2 = new_row * taille
            fenetre.blit(sprite_jaune2, (x_jaune2, y_jaune2))

    # Placer le sprite Jaune autour du sprite Rouge
    for direction in [(1, -5), (1, 5), (-5, 1), (5, 1), (4, -5), (4, 5), (-5, 4), (5, 4), (-4, -5), (-4, 5),
                      (-5, -4), (5, -4), (5, -5), (5, 5), (-5, 5), (5, 5), (-5, -5), (-5, 5), (-5, -5), (5, -5),
                      (3, -5), (3, 5), (-5, 3), (5, 3), (-3, -5), (-3, 5), (-5, -3), (5, -3), (2, -5), (2, 5),
                      (-5, 2), (5, 2), (-2, -5), (-2, 5), (-5, -2), (5, -2), (1, -5), (1, 5), (-5, 1), (5, 1),
                      (-1, -5), (-1, 5), (-5, -1), (5, -1), (0, -5), (0, 5), (-5, 0), (5, 0), (-0, -5), (-0, 5),
                      (-5, -0), (5, -0), (-5, -5), (-5, 5), (5, -5), (5, 5)]:
        dx, dy = direction
        new_row = ligne_rouge + dy
        new_col = colonne_rouge + dx
        if 1 <= new_row < n and 0 <= new_col < n:
            sprite_jaune = pygame.image.load(Jaune).convert()
            sprite_jaune = pygame.transform.scale(sprite_jaune, (taille, taille))
            x_jaune = new_col * taille
            y_jaune = new_row * taille
            fenetre.blit(sprite_jaune, (x_jaune, y_jaune))

    # Placer le sprite Vert autour du sprite Rouge
    for direction in [(1, -6), (1, 6), (-6, 1), (6, 1), (4, -6), (4, 6), (-6, 4), (6, 4), (-4, -6), (-4, 6),
                      (-6, -4), (6, -4), (6, -6), (6, 6), (-6, 6), (6, 6), (-6, -6), (-6, 6), (-6, -6), (6, -6),
                      (5, -6), (5, 6), (-6, 5), (6, 5), (-5, -6), (-5, 6), (-6, -5), (6, -5), (3, -6), (3, 6),
                      (-6, 3), (6, 3), (-3, -6), (-3, 6), (-6, -3), (6, -3), (2, -6), (2, 6), (-6, 2), (6, 2),
                      (-2, -6), (-2, 6), (-6, -2), (6, -2), (1, -6), (1, 6), (-6, 1), (6, 1), (-1, -6), (-1, 6),
                      (-6, -1), (6, -1), (0, -6), (0, 6), (-6, 0), (6, 0), (-0, -6), (-0, 6), (-6, -0), (6, -0),
                      (-6, -6), (-6, 6), (6, -6), (6, 6)]:
        dx, dy = direction
        new_row = ligne_rouge + dy
        new_col = colonne_rouge + dx
        if 1 <= new_row < n and 0 <= new_col < n:
            sprite_vert = pygame.image.load(Vert).convert()
            sprite_vert = pygame.transform.scale(sprite_vert, (taille, taille))
            x_vert = new_col * taille
            y_vert = new_row * taille
            fenetre.blit(sprite_vert, (x_vert, y_vert))

    # Placer le sprite Vert2 autour du sprite Rouge
    for direction in [(1, -7), (1, 7), (-7, 1), (7, 1), (4, -7), (4, 7), (-7, 4), (7, 4), (-4, -7), (-4, 7),
                      (-7, -4), (7, -4), (7, -7), (7, 7), (-7, 7), (7, 7), (-7, -7), (-7, 7), (-7, -7), (7, -7),
                      (6, -7), (6, 7), (-7, 6), (7, 6), (-6, -7), (-6, 7), (-7, -6), (7, -6), (5, -7), (5, 7),
                      (-7, 5), (7, 5), (-5, -7), (-5, 7), (-7, -5), (7, -5), (3, -7), (3, 7), (-7, 3), (7, 3),
                      (-3, -7), (-3, 7), (-7, -3), (7, -3), (2, -7), (2, 7), (-7, 2), (7, 2), (-2, -7), (-2, 7),
                      (-7, -2), (7, -2), (1, -7), (1, 7), (-7, 1), (7, 1), (-1, -7), (-1, 7), (-7, -1), (7, -1),
                      (0, -7), (0, 7), (-7, 0), (7, 0), (-0, -7), (-0, 7), (-7, -0), (7, -0), (-7, -7), (-7, 7),
                      (7, -7), (7, 7)]:
        dx, dy = direction
        new_row = ligne_rouge + dy
        new_col = colonne_rouge + dx
        if 1 <= new_row < n and 0 <= new_col < n:
            sprite_vert2 = pygame.image.load(Vert_2).convert()
            sprite_vert2 = pygame.transform.scale(sprite_vert2, (taille, taille))
            x_vert2 = new_col * taille
            y_vert2 = new_row * taille
            fenetre.blit(sprite_vert2, (x_vert2, y_vert2))

    # Placer le sprite Bleu2 autour du sprite Rouge
    for direction in [(1, -8), (1, 8), (-8, 1), (8, 1), (4, -8), (4, 8), (-8, 4), (8, 4), (-4, -8), (-4, 8),
                      (-8, -4), (8, -4), (8, -8), (8, 8), (-8, 8), (8, 8), (-8, -8), (-8, 8), (-8, -8), (8, -8),
                      (6, -8), (6, 8), (-8, 6), (8, 6), (-6, -8), (-6, 8), (-8, -6), (8, -6), (7, -8), (7, 8),
                      (-8, 7), (8, 7), (-7, -8), (-7, 8), (-8, -7), (8, -7), (5, -8), (5, 8), (-8, 5), (8, 5),
                      (-5, -8), (-5, 8), (-8, -5), (8, -5), (3, -8), (3, 8), (-8, 3), (8, 3), (-3, -8), (-3, 8),
                      (-8, -3), (8, -3), (2, -8), (2, 8), (-8, 2), (8, 2), (-2, -8), (-2, 8), (-8, -2), (8, -2),
                      (1, -8), (1, 8), (-8, 1), (8, 1), (-1, -8), (-1, 8), (-8, -1), (8, -1), (0, -8), (0, 8),
                      (-8, 0), (8, 0), (-0, -8), (-0, 8), (-8, -0), (8, -0), (-8, -8), (-8, 8), (8, -8),
                      (8, 8)]:
        dx, dy = direction
        new_row = ligne_rouge + dy
        new_col = colonne_rouge + dx
        if 1 <= new_row < n and 0 <= new_col < n:
            sprite_bleu2 = pygame.image.load(Bleu_2).convert()
            sprite_bleu2 = pygame.transform.scale(sprite_bleu2, (taille, taille))
            x_bleu2 = new_col * taille
            y_bleu2 = new_row * taille
            fenetre.blit(sprite_bleu2, (x_bleu2, y_bleu2))

    # Placer le sprite Bleu autour du sprite Rouge
    for direction in [(1, -9), (1, 9), (-9, 1), (9, 1), (4, -9), (4, 9), (-9, 4), (9, 4), (-4, -9), (-4, 9),
                      (-9, -4), (9, -4), (9, -9), (9, 9), (-9, 9), (9, 9), (-9, -9), (-9, 9), (-9, -9), (9, -9),
                      (6, -9), (6, 9), (-9, 6), (9, 6), (-6, -9), (-6, 9), (-9, -6), (9, -6), (7, -9), (7, 9),
                      (-9, 7), (9, 7), (-7, -9), (-7, 9), (-9, -7), (9, -7), (5, -9), (5, 9), (-9, 5), (9, 5),
                      (-5, -9), (-5, 9), (-9, -5), (9, -5), (8, -9), (8, 9), (-9, 8), (9, 8), (-8, -9), (-8, 9),
                      (-9, -8), (9, -8), (3, -9), (3, 9), (-9, 3), (9, 3), (-3, -9), (-3, 9), (-9, -3), (9, -3),
                      (2, -9), (2, 9), (-9, 2), (9, 2), (-2, -9), (-2, 9), (-9, -2), (9, -2), (1, -9), (1, 9),
                      (-9, 1), (9, 1), (-1, -9), (-1, 9), (-9, -1), (9, -1), (0, -9), (0, 9), (-9, 0), (9, 0),
                      (-0, -9), (-0, 9), (-9, -0), (9, -0), (-9, -9), (-9, 9), (9, -9), (9, 9)]:
        dx, dy = direction
        new_row = ligne_rouge + dy
        new_col = colonne_rouge + dx
        if 1 <= new_row < n and 0 <= new_col < n:
            sprite_bleu = pygame.image.load(Bleu).convert()
            sprite_bleu = pygame.transform.scale(sprite_bleu, (taille, taille))
            x_bleu = new_col * taille
            y_bleu = new_row * taille
            fenetre.blit(sprite_bleu, (x_bleu, y_bleu))

    pygame.image.save(fenetre, "Images/plateau.jpg")
    #pygame.display.flip() POUR AFFICHER LA SOLUTION

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

    while running and compteur<15:

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
musique()
affiche_all()
plateau(largeur, hauteur, n)
affiche_solution()
fond_plateau_solution()
attente_clic()
pygame.quit()




