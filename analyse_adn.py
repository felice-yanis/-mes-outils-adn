def analyse_adn(adn):
    adn = adn.upper().strip()
    gc = (adn.count("G") + adn.count("C")) / len(adn) * 100
    return len(adn), round(gc, 2)

sequence = "  atcgttagctag  "
longueur, gc = analyse_adn(sequence)

print(f"Longueur nettoyee : {longueur}")
print(f"%GC : {gc}%")
