from math import factorial


def calcola(numero_dadi: int, totale_dadi: int, perudo: bool = False) -> float:
    """
    C = n! / [ k!(n-k)!]

    n = totale_dadi
    k = numero di dadi uguali
    """
    p = 1 / 6

    if perudo == True:
        p = 2 / 6

    neg_p = 1 - p

    n_fact = factorial(totale_dadi)

    k_fact = factorial(numero_dadi)

    C = n_fact / (k_fact * factorial(totale_dadi - numero_dadi))

    P = C * p**numero_dadi * neg_p ** (totale_dadi - numero_dadi)

    return P


if __name__ == "__main__":
    while True:

        numero_dadi = input(
            "Inserisci il numero di dadi che devono avere lo stesso valore o Q per uscire: "
        )
        if numero_dadi.lower() == "q":
            break

        try:
            numero_dadi = int(numero_dadi)
        except ValueError:
            print("Valore non valido, riprova")
            continue

        totale_dadi = input(
            "Inserisci il totale dei dadi a disposizione o Q per uscire: "
        )

        if totale_dadi.lower() == "q":
            break

        try:
            totale_dadi = int(totale_dadi)
        except ValueError:
            print("Valore non valido, riprova")
            continue

        perudo = input(
            "Inserisci P se i perudo valgono oppure N se non valgono o Q per uscire: "
        )

        match perudo:
            case "Q":
                break
            case "q":
                break
            case "P":
                perudo = True
            case "p":
                perudo = True
            case "N":
                perudo = False
            case "n":
                perudo = False
            case _:
                continue

        result = calcola(
            numero_dadi=int(numero_dadi),
            totale_dadi=int(totale_dadi),
            perudo=bool(perudo),
        )

        print(
            f"""La probabilità che ci siano {numero_dadi} su {totale_dadi}\n
            con lo stesso valore ({"con perudo" if perudo else "senza perudo"}) è: \n{round(result,2)*100}%"""
        )


