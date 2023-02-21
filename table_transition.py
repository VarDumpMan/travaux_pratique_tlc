# -*- coding:utf8 -*-

from modules.functions import *

# Variables

table_transition = {}

alphabet = []
etats = []
etat_initial = ""
etats_finaux = []



print("Nous voulons prendre votre automate sous la forme de la table de transition ! De ce fait, nous allons suivre plusieurs étapes !\n")

# Entrée des lettres de l'alphabet 

print("Vous allez renseigner les lettres de l'alphabet de votre langage ! \nVous pouvez marquer la fin des lettres de l'alphabet en tapant 'fin' !\n NB : £ représente epsilonne dans l'algorithme !")

entree_information("Entrer une lettre de l'alphabet de votre langage : ", alphabet, "Votre alphabet : {}")

# Entrée des états 

print("\nVous allez renseigner les états pour obtenir les mots de votre langage ! \nVous pouvez marquer la fin des états en tapant 'fin' !\n")

entree_information("Entrer un état (sous forme q1 ou q2...) : ", etats, "Vos états : {}")

# Renseigner l'etat initial

entree = input("Renseigner l'état initial : ")

while(entree not in etats):
    entree = input("Renseigner le bon état initial : ")

etat_initial = entree

# Renseigner le ou les états finaux

nbre_finaux = int(input("Entrer le nombre d'états finaux : "))

for i in range(nbre_finaux):
    
    entree = input("Entrer un état final : ")
    
    while(entree not in etats):
        entree = input("Entrer un bon état final : ")
        
    etats_finaux.append(entree)

# Remplissage de la table de transition 

print("Nous allons à présent associer à chaque état une ou des valeurs pour une lettre de l'alphabet ! \nSi vous avez plusieurs états à associer, séparez-les par des virgules")

for etat in etats:
    
    table_transition_element = {}
    
    for lettre in alphabet:
        
        entree = input("Entrer la transition de " + etat + " pour " + lettre + " : \n")
        
        table_transition_element[lettre] = entree
             
        pass
    
    pass

    table_transition[etat] = table_transition_element

print(table_transition)

print("\nVoici notre table de transition :\n")
affichage_table_transition(table_transition=table_transition, etats=etats, alphabets=alphabet)


# Identification de l'automate et Transformation en AFD

if(identification_afn(alphabets=alphabet, etats=etats, table_transition=table_transition)):
    
    print("Cet automate est un AFN")
    
    
    
if(identification_afd(alphabets=alphabet, etats=etats, table_transition=table_transition)):
    print("Cet automate est déjà un AFD.")
if(identification_eafn(alphabets=alphabet)):
    print("Cet automate est un £-AFN")
    pass


