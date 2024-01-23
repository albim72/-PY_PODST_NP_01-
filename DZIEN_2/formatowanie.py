tekst = "to jest test!"
cyfra = 8
nr = 8897

info = "informacja nr {2}: {0}, wybrana cyfra: {1}"
#ekstrapolacja wartości string 'teskt' wewnątrz wartośc 'info' -> {}

print(info.format(tekst,cyfra,nr))
