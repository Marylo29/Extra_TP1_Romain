def romain(valeur):
    valeur = int(valeur)
    txt = ""
    while valeur > 0:
        if valeur >= 1000:
            txt += "M"
            valeur -= 1000
        elif valeur >= 900:
            txt += "CM"
            valeur -= 900
        elif valeur >= 500:
            txt += "D"
            valeur -= 500
        elif valeur >= 400:
            txt += "CD"
            valeur -= 400
        elif valeur >= 100:
            txt += "C"
            valeur -= 100
        elif valeur >= 90:
            txt += "XC"
            valeur -= 90
        elif valeur >= 50:
            txt += "L"
            valeur -= 50
        elif valeur >= 40:
            txt += "XL"
            valeur -= 40
        elif valeur >= 10:
            txt += "X"
            valeur -= 10
        elif valeur >= 9:
            txt += "IX"
            valeur -= 9
        elif valeur >= 5:
            txt += "V"
            valeur -= 5
        elif valeur >= 4:
            txt += "IV"
            valeur -= 4
        elif valeur >= 1:
            txt += "I"
            valeur -= 1
    return txt
        


# Tests
assert romain(4) == "IV"
assert romain(5) == "V"
assert romain(6) == "VI"
assert romain(4042) == "MMMMXLII"