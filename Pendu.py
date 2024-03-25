import random

# Liste de mots à deviner
mots = ["python", "ordinateur", "pendu", "programmation", "codage"]

# Choisir un mot aléatoirement de la liste
mot_a_deviner = random.choice(mots)
lettres_trouvees = ['_'] * len(mot_a_deviner)
tentatives_restantes = 7

print("Bienvenue dans le jeu du Pendu !")
print("".join(lettres_trouvees))

while tentatives_restantes > 0 and '_' in lettres_trouvees:
    lettre = input("Devinez une lettre: ").lower()

    if lettre in mot_a_deviner:
        for i in range(len(mot_a_deviner)):
            if mot_a_deviner[i] == lettre:
                lettres_trouvees[i] = lettre
        print("Bonne réponse: " + "".join(lettres_trouvees))
    else:
        tentatives_restantes -= 1
        print(f"Mauvaise réponse. Il vous reste {tentatives_restantes} tentatives.")

    if '_' not in lettres_trouvees:
        print("Félicitations ! Vous avez trouvé le mot :", mot_a_deviner)
        break

if tentatives_restantes == 0:
    print("Désolé, vous avez perdu. Le mot était :", mot_a_deviner)
