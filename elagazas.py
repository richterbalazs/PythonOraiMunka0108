def hossz():

    szo = input("\t Kérek egy szót: ") # \t azért kell hogy egy tabulátorral beljebb kezdődjön!
    szo2 = input("\t Kérek egy másik szót: ") # /t azért kell hogy egy tabulátorral beljebb kezdődjön!

    szoHossz = len(szo)
    szo2Hossz = len(szo2)
    print("I/a.")

    if szoHossz < szo2Hossz:
        print(f"\t A hosszab szó: {szo2}.")
    elif szoHossz > szo2Hossz:
        print(f"\t A hosszabb szó: {szo}.")
    else:
        print("\t A két szó hossza egyenlő: .")
    print("I/b.")
    kulonbseg = abs(szoHossz-szo2Hossz) # abszolút értékhez kell az abs!
    print(f"\t A szavak hosszának a különbsége: {kulonbseg}.")