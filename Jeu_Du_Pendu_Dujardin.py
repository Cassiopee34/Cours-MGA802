import random
##Consignes: Pour ce mini projet , vous allez écrire un code qui permet de jouer au jeu du pendu contre votre programme! Votre programme doit être composé de fonctions seulement

## Fonction pour choisir un mot au hasard dans la liste de mots

def choisir_mot ():
    mots = []
    with open("mots_pendu.txt",'r') as f:
# Permet de lire le documents contenant les différents mots du pendu
        mots = f.readlines()
#on utilise readlines à la place de juste read car ainsi on peut séparer les mots en fonctions de quand ils reviennent à la ligne
    return random.choice (mots).strip()


## Fonction qui lance le jeu du pendu, contient aussi la boucle principale

def jouer_au_pendu():
#Initialisation des variables nécéssaires
    mot_aleatoire = choisir_mot ()
    lettres_trouvees = []
    nombre_de_chances = 6

#Début de la boucle pour jouer, tant que le joueur a encore des chances
    while nombre_de_chances > 0:
        print ("Il vous reste ",nombre_de_chances," chances")
#Utilise la fonction qui affiche le mot, ici il sera affiché avec des tirets pour savoir le nombre de lettres à deviner
        afficher_mot(mot_aleatoire, lettres_trouvees)
        lettre = choix_de_lettre()

        if lettre in mot_aleatoire:
            print("Cette lettre fait bien partie du mot !")
#On ajoute la nouvelle lettre devinée dans la liste de celles trouvées, ainsi on pourra comparer cette liste avec le mot_aleatoire
            lettres_trouvees.append(lettre)
#On compare les 2 pour vérifier si le joueur à gagner
            if set(mot_aleatoire) == set(lettres_trouvees):
                print("Bravo, vous avez gagné ! Vous avez deviné le mot qui était ",mot_aleatoire)
                return

        else:
            print("Cette lettre ne fait pas partie du mot")
# on décrémente le curseur nombres_de_chances
            nombre_de_chances = nombre_de_chances - 1

    print ("Vous avez perdu, le mot était : ", mot_aleatoire)


##Fonction qui permet d'afficher le mot
#permet soit d'afficher des tirets pour deviner les lettres, soit d'afficher les lettre trouvées
def afficher_mot(mot_aleatoire,lettres_trouvees):
    mot_affiche = ""
    for lettre in mot_aleatoire:
        if lettre in lettres_trouvees:
            mot_affiche = mot_affiche + lettre
        else:
            mot_affiche = mot_affiche + "_ "
    print(mot_affiche)

##Fonction qui demande au joueur ces différents choix de lettres

def choix_de_lettre():
    lettre = input ("Choisissez une lettre pour deviner le mot : ")
    return lettre

## Cette ligne de code permet de commencer à jouer

jouer_au_pendu()
