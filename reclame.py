from algemene_functies import mijn_fuctie_2

def combienatie(invoer_lijst2):
     korte_lijst = laag_en_hoog(invoer_lijst2)
     return mijn_fuctie_2(korte_lijst[0], korte_lijst[1])

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)

    return (
        f"Vandaag in de aanbieding: emmertje ijs (1 liter) "
        f"in de smaak {smaak}, van {prijs} euro voor "
        f"{nieuwe_prijs:.2f} euro." 
    )


def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw

    return (
        f"Het totaal van alle inkomsten van deze week is "
        f"{totaal} euro, waarover {btw_bedrag} euro btw "
        f"betaald dient te worden."
    )


def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

def gemiddelde(mijn_lijst):
    gemiddelde_bedrag = sum(mijn_lijst) / len(mijn_lijst)

    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_bedrag} euro."

def meervoudig(invoer_lijst):
        return laag_en_hoog(invoer_lijst)