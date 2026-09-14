def compter_bases(adn):
    adn = adn.upper().strip()
    a = adn.count("A")
    t = adn.count("T")
    c = adn.count("C")
    g = adn.count("G")
    
    total = len(adn)
    print(f"Séquence : {adn}")
    print(f"Longueur : {total} bases")
    print(f"A : {a} | T : {t} | C : {c} | G : {g}")

compter_bases("  ATTCGGATTCCGATATATAG  ")
