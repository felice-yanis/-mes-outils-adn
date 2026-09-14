from analyse_adn import analyse_adn
from compteur_bases import compter_bases
from detecteur_anomalie import verifier_adn

sequence = "  ATTCGGATTCCGATATAG  "

print("--- ANALYSE BIO-INFORMATIQUE ---")

if verifier_adn(sequence):
    longueur, gc = analyse_adn(sequence)
    print(f"Longueur : {longueur} | %GC : {gc}%")
    compter_bases(sequence)
