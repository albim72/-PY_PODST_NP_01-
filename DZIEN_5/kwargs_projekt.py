def moja_funkcja_z_lista_args(argument1,*argv):
    print(f"pierwszy argument funkcji: {argument1}")
    for arg in argv:
        print(f"następny argument z  listy *argv: {arg}")


moja_funkcja_z_lista_args('Krótka informacja: A',True,564,"Olsztyn",3.33)


def moja_funkcja_ze_slownikiem_args(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} => {value}")


moja_funkcja_ze_slownikiem_args(pierwszy='Roman',drugi='Opel',taki=456,inny=0.55)
