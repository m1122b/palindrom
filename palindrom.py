
def palindrom(word: str):
    """"
        Opis:
        Sprawdza litere po literze od przodu i od tyłu czy są równe jeżeli tak wpisuje
        do listy Prawda jeżeli nie wpisuje do listy Nieprawda.
        Na koniec sprawdzamy czy w w liście są same prawdy.
    """
    results = []
    
    for i in range(len(word)):
        first_letter = word[i]
        last_letter = word[-1-i]
        
        if first_letter == last_letter:
            results.append(True)
        else:
            results.append(False)

    if all(results):
        result = True
    else:
        result = False

    return result


word = "Argument funkcji"
print(palindrom(word))
print(type(palindrom(word)))
print("")

word = "kajak"
print(palindrom(word))
print(type(palindrom(word)))
print("")

