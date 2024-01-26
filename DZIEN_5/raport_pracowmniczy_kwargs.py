def wygeneruj_raport_pracowniczy(**kwargs):
    raport = "Raport Pracowniczy:\n"

    for key, value in kwargs.items():
        raport += f'{key}: {value}\n'

    return raport

info_pracownik_1 ={
    "imię": "Jan",
    "nazwisko": "Kot",
    "stanowisko": "inżynier sieci IT",
    "dział firmy": "IT",
    "wynagrodzenie": 15400,
    "doświadczenie [lata]": 13
}

info_pracownik_2 ={
    "imię": "Anna",
    "nazwisko": "Nowak",
    "stanowisko": "Dyrektor finansowy",
    "dział firmy": "Finanse",
    "wynagrodzenie": 23400,
    "doświadczenie [lata]": 28,
    "wykształcenie":"stopień doktora ekonomii (Uniwersytet Śląski)",
    "dodatkowe funkcje":"honorowy prezes fundacji EKO"
}

raport_1 = wygeneruj_raport_pracowniczy(**info_pracownik_1)
print(raport_1)

print("_______________________________________________________")

raport_2 = wygeneruj_raport_pracowniczy(**info_pracownik_2)
print(raport_2)
