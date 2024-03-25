import pytest
from pendu import choisir_mot, traiter_tentative  # Assurez-vous que pendu.py est accessible

# Votre liste de mots pourrait être importée ou définie directement dans test_pendu.py pour les tests
mots = ["python", "ordinateur", "pendu", "programmation", "codage"]

def test_choisir_mot():
    """Teste si choisir_mot renvoie un mot de la liste mots."""
    mot = choisir_mot()
    assert mot in mots, "Le mot choisi doit être dans la liste des mots disponibles."

def test_traiter_tentative():
    """Teste la fonction traiter_tentative avec une lettre correcte et incorrecte."""
    mot_a_deviner = "python"
    lettres_trouvees = ['_'] * len(mot_a_deviner)
    # Test avec une lettre correcte
    assert traiter_tentative(mot_a_deviner, 'p', lettres_trouvees), "Doit renvoyer True pour une lettre correcte."
    assert lettres_trouvees == ['p', '_', '_', '_', '_', '_'], "La lettre correcte 'p' doit être ajoutée aux lettres trouvées."
    # Test avec une lettre incorrecte
    resultat = traiter_tentative(mot_a_deviner, 'z', lettres_trouvees)
    assert not resultat, "Doit renvoyer False pour une lettre incorrecte."
    assert lettres_trouvees == ['p', '_', '_', '_', '_', '_'], "Aucune lettre ne doit être ajoutée pour une tentative incorrecte."
