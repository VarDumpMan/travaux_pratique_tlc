# -*- coding:utf8 -*-

# Fonctions

# Récupération d'une liste de valeur insérée au fur et à mesure dans un tableau

def entree_information(message_entree, tableau, message_fin):
    entre = input(message_entree)

    while (entre != 'fin'):

        if (entre not in tableau):
            tableau.append(entre)

        entre = input(message_entree)

    print(message_fin.format(tableau))


# Identification d'un £-afn

def identification_eafn(alphabets):

    if ("£" in alphabets):

        return True

    else:

        return False

    pass

# Identification d'un afn


def identification_afn(alphabets,  etats, table_transition):

    if (not identification_eafn(alphabets)):

        # Parcours de la table de transition

        for etat in etats:

            for lettre in alphabets:

                lettre_correspondante = table_transition[etat][lettre]

                liste_element_correspondant = lettre_correspondante.split(",")

                if (len(liste_element_correspondant) > 1):
                    return True

            pass

        return False

    else:

        return False

# Identification d'un afd


def identification_afd(alphabets, etats, table_transition):

    if (not identification_afn(alphabets=alphabets, etats=etats, table_transition=table_transition) and not identification_eafn(alphabets)):

        return True

        pass

    else:

        return False

# Affichage de la table de transition


def affichage_table_transition(table_transition, etats, alphabets):

    print("---------Affichage de la table de transition---------\n")

    entete = "|Etats \t|"

    for lettre in alphabets:

        entete += lettre + "\t|"

    print(entete)

    content = ""

    for etat in etats:

        content = "|" + etat + "\t|"

        for lettre in alphabets:

            content += table_transition[etat][lettre] + "\t|"

        print(content)

    pass

# Transformation AFN en AFD


def transformation_afn_afd(table_transition, etat_initial):

    liste_etats = [etat_initial]
    deja_parcouru = []

    while (len(liste_etats) > 0):
        firsts = liste_etats[0].split(",")
                
        if(len(firsts) > 1):
            
            for first in firsts:
                
                first = first.strip()
                
                if len(first) > 0 and first not in deja_parcouru:
                    
                    etats_transition = table_transition[first]
                    deja_parcouru.append(first)

                    liste_etats = liste_etats[1:len(liste_etats)]

                    for etat in etats_transition.values():

                        liste_etats.append(etat)
                        print(liste_etats)
                        
                
        else:
            
            first = firsts[0].strip()
                        
            if len(first) > 0 and first not in deja_parcouru:

                etats_transition = table_transition[first]
                deja_parcouru.append(first)

                liste_etats = liste_etats[1:len(liste_etats)]

                for etat in etats_transition.values():

                    liste_etats.append(etat)
            else:
                break
            pass
        
        
                
    #print(firsts)
            
    print(f"Liste : {liste_etats}")
    print(f"Deja parcouru : {deja_parcouru}")

    pass
