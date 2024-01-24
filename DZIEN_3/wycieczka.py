def kwota(t,nw,w,u,i,rab=0):
    if rab>=0 and rab <= 70:
        return (nw+t)*(1-rab/100)+w+u+i
    else:
        return "podaj rabat z przedziału 1% - 70%"

print("kwota do zapłaty:",kwota(100,100,50,50,50),"zł")
print("kwota do zapłaty:",kwota(100,100,50,50,50,25),"zł")
print("kwota do zapłaty:",kwota(100,100,50,50,50,75),"zł")
