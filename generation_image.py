#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt

def main():
    # Vérification du nombre d'arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <nom_fichier> <n>")
        sys.exit(1)
    
    nom_fichier = sys.argv[1]
    try:
        n_total = int(sys.argv[2])
    except ValueError:
        print("Le second argument doit être un entier.")
        sys.exit(1)
    
    # Lecture du fichier et extraction des données
    try:
        with open(nom_fichier, 'r') as f:
            lignes = f.readlines()
    except FileNotFoundError:
        print(f"Erreur : le fichier '{nom_fichier}' n'existe pas.")
        sys.exit(1)
    
    if len(lignes) < 2:
        print("Erreur : le fichier doit contenir exactement deux lignes.")
        sys.exit(1)
    
    # Première ligne : liste des valeurs
    valeurs = lignes[0].strip().split()
    # Deuxième ligne : occurrences associées à chaque valeur
    try:
        occurrences = [int(x) for x in lignes[1].strip().split()]
    except ValueError:
        print("Erreur : la deuxième ligne doit contenir des entiers.")
        sys.exit(1)
    
    # Vérification que le nombre de valeurs correspond au nombre d'occurrences
    if len(valeurs) != len(occurrences):
        print("Erreur : le nombre de valeurs et le nombre d'occurrences doivent être identiques.")
        sys.exit(1)
    
    # Vérification que la somme des occurrences est égale à n
    if sum(occurrences) != n_total:
        print(f"Erreur : la somme des occurrences ({sum(occurrences)}) ne correspond pas à n ({n_total}).")
        sys.exit(1)
    
    # Calcul des pourcentages d'apparition (avec 2 décimales)
    pourcentages = [(occ / n_total) * 100 for occ in occurrences]
    
    # Configuration globale (taille de police, etc.)
    plt.rcParams.update({'font.size': 14})
    
    # Création du graphique (taille plus grande)
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Positions pour les barres
    positions = range(len(valeurs))
    largeur_barres = 0.7
    
    # Ajout du paramètre 'hatch' pour créer des barres obliques
    bars = ax.bar(
        positions, 
        pourcentages, 
        color='skyblue', 
        width=largeur_barres,
        edgecolor='black',  # Pour mieux voir le contour
        hatch='//'          # Motif diagonal : '/', '//', '\', '\\', etc.
    )
    
    # Configuration de l'axe X
    ax.set_xticks(positions)
    ax.set_xticklabels(valeurs)
    
    # Titres et labels
    ax.set_xlabel("Valeurs", fontsize=14)
    ax.set_ylabel("Fréquence (%)", fontsize=14)
    ax.set_title("Fréquence d'apparition de chaque valeur", fontsize=16)
    
    # Ajustement de la limite supérieure de l'axe Y (pour laisser la place aux étiquettes)
    y_max = max(pourcentages) if pourcentages else 0
    ax.set_ylim(0, y_max + 0.35 * y_max if y_max > 0 else 1)
    
    # Placement des pourcentages au-dessus de chaque barre
    offset = 0.02 * y_max
    for i, p in enumerate(pourcentages):
        ax.text(
            i, 
            p + offset, 
            f"{p:.2f}%", 
            ha='center', 
            va='bottom', 
            fontsize=13,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=3)
        )
    
    plt.tight_layout()
    plt.savefig("histogramme.png")
    plt.show()
    print("L'image a été sauvegardée sous le nom 'histogramme.png'.")

if __name__ == "__main__":
    main()
