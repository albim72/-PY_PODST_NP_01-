#funckja wyższego rzędu

def message(msg):
    return f'pobrana infromacja: {msg}'

def multiinfo(msg,wart,wsp):
    return f'{msg} -> {wart*wsp}'

def infoset(funkcja,*args):
    return funkcja(*args)

print(infoset(message,"tysiące liczb - 42342 343"))
print(infoset(multiinfo,"mnożenie dwóch wartości",56,3))
