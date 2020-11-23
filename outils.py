from fourni.minotaure import Minotaure
from fourni.case_vide import CaseVide
from fourni.sortie import Sortie
from fourni.mur import Mur
from fourni.personnage import Personnage

DISTANCE_ENTRE_CASE = 32
X_PREMIERE_CASE = 20

def creer_image(can, x: int, y: int, image: object):
    """
    Fonction qui permet de créer/remplacer une image dans le canvas. Pour l'utiliser il faut préciser :
    :param can: un canvas (faites abstraction de ce que c'est et marquez : can
    :param x: une coordonnée dans l'axe des abscisses ( coordonnée x)
    :param y: une coordonnée dans l'axe des ordonnées ( coordonnée y)
    :param image: une image tirée de la liste d'image (voir énoncé pour quelle image choisir via quel index)
    :return:
    """
    can.create_image(x* DISTANCE_ENTRE_CASE + X_PREMIERE_CASE, y* DISTANCE_ENTRE_CASE + X_PREMIERE_CASE, image=image)


def creer_mur(x: int, y: int) -> Mur:
    """
    Fonction permettant de créer un mur.
    :param x: coordonnée en x du mur à créer
    :param y:coordonnée en y du mur à créer
    :return: la variable mur
    """
    return Mur(x, y)


def creer_minotaure(x: int, y: int) -> Minotaure:
    """
    Fonction permettant de créer un minotaure.
    :param x: coordonnée en x du minotaure à créer
    :param y:coordonnée en y du minotaure à créer
    :return: la variable minotaure
    """
    return Minotaure(x, y)


def creer_sortie(x: int, y: int)-> Sortie:
    """
    Fonction permettant de créer une Sortie.
    :param x: coordonnée en x de la Sortie à créer
    :param y:coordonnée en y de la Sortie à créer
    :return: la variable Sortie
    """
    return Sortie(x, y)


def creer_personnage(x: int, y: int) -> Personnage:
    """
    Fonction permettant de créer un personnage.
    :param x: coordonnée en x du personnage à créer
    :param y:coordonnée en y du personnage à créer
    :return: la variable personnage
    """
    return Personnage(x, y)


def creer_case_vide(x: int, y: int) -> CaseVide:
    """
    Fonction permettant de créer une case vide.
    :param x: coordonnée en x de la case vide à créer
    :param y:coordonnée en y de la case vide à créer
    :return: la variable case vide
    """
    return CaseVide(x, y)


def coordonnee_x(variable: object) -> int:
    """
    Fonction permettant de retourner la coordonnée en x de la variable.
    :param variable: la variable (Personnage,Minotaure, CaseVide, Sortie, Mur)
    :return: la coordonnée en x de la variable
    """
    return variable.get_x()


def coordonnee_y(variable: object) -> int:
    """
    Fonction permettant de retourner la coordonnée en y de la variable.
    :param variable: la variable (Personnage,Minotaure, CaseVide, Sortie, Mur)
    :return: la coordonnée en y de la variable
    """
    return variable.get_y()


def est_egal_a(variable1: object, variable2: object) -> bool:
    """
    Fonction permettant de tester l'égalité entre 2 variables (Personnage, Minotaure, CaseVide, Sortie, Mur)
    :param variable1: variable (Personnage, Minotaure, CaseVide, Sortie, Mur)
    :param variable2: variable (Personnage, Minotaure, CaseVide, Sortie, Mur)
    :return: Booléen (True si les deux variables sont identiques, False sinon)
    """
    return variable1 == variable2
