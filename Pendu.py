import random
import pytest

# Liste de mots à deviner
mots = ["python", "ordinateur", "pendu", "programmation", "codage"]

def choisir_mot():
    """Choisit un mot aléatoirement de la liste."""
    return random.choice(mots)

def afficher_mot(mot_a_deviner, lettres_trouvees):
    """Affiche l'état actuel du mot à deviner avec les lettres trouvées."""
    affichage = ''.join([lettre if lettre in lettres_trouvees else '_' for lettre in mot_a_deviner])
    print(affichage)

def traiter_tentative(mot_a_deviner, tentative, lettres_trouvees):
    """Met à jour les lettres trouvées basé sur la tentative du joueur."""
    if tentative in mot_a_deviner:
        for i in range(len(mot_a_deviner)):
            if mot_a_deviner[i] == tentative:
                lettres_trouvees[i] = tentative
        return True
    return False

def jouer_pendu():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = ['_'] * len(mot_a_deviner)
    tentatives_restantes = 7

    print("Bienvenue dans le jeu du Pendu !")
    afficher_mot(mot_a_deviner, lettres_trouvees)

    while tentatives_restantes > 0 and '_' in lettres_trouvees:
        tentative = input("Devinez une lettre: ").lower()

        if not traiter_tentative(mot_a_deviner, tentative, lettres_trouvees):
            tentatives_restantes -= 1
            print(f"Mauvaise réponse. Il vous reste {tentatives_restantes} tentatives.")
        afficher_mot(mot_a_deviner, lettres_trouvees)

        if '_' not in lettres_trouvees:
            print("Félicitations ! Vous avez trouvé le mot :", mot_a_deviner)
            return

    print("Désolé, vous avez perdu. Le mot était :", mot_a_deviner)

if __name__ == "__main__":
    jouer_pendu()
