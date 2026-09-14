def verifier_adn(adn):
    adn = adn.upper().strip()
    bases_valides = "ATCG"
    anomalie_trouvee = False

    for lettre in adn:
        if lettre not in bases_valides:
            print(f"⚠️ ANOMALIE DETECTEE : '{lettre}' n'est pas une base ADN valide !")
            anomalie_trouvee = True
    
    if not anomalie_trouvee:
        print(f"✅ Séquence OK : {adn} est propre.")
        return True
    else:
        print(f"❌ Séquence à rejeter.")
        return False

verifier_adn("ATTCGATT")
verifier_adn("ATTCGXTZ  ")
