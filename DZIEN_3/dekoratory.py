#funckja wyższego rzędu

def message(msg):
    return f'pobrana infromacja: {msg}'

def multiinfo(msg,wart,wsp):
    return f'{msg} -> {wart*wsp}'

def infoset(funkcja,*args):
    return funkcja(*args)

print(infoset(message,"tysiące liczb - 42342 343"))
print(infoset(multiinfo,"mnożenie dwóch wartości",56,3))

#funkcja dekorująca

def startstop(funkcja):
    def wrapper(*args):
        print("startowanie procesu....")
        funkcja(*args)
        print("kończenie procesu....")
    return wrapper

def zawijanie(czego):
    print(f'zawijanie {czego} w sreberka!')


zw = startstop(zawijanie)
zw("czekoladek")

@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} na urodzinowym torcie!")

dmuchanie("świeczek")

