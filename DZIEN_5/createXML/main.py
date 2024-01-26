from xml.etree.ElementTree import Element,SubElement
from prettyfy import pretty

top = Element('autokomis')

#pierwszy samochód
sam1 = SubElement(top,'samochod')

id = SubElement(sam1,'id')
id.text = 'sam1'

marka = SubElement(sam1,'marka')
marka.text = 'Subaru'

model = SubElement(sam1,'model')
model.text = 'Impreza'

rok = SubElement(sam1,'rocznik')
rok.text = '2000'

poj = SubElement(sam1,'pojemnosc')
poj.text = '2.0'

cena = SubElement(sam1,'cena')
cena.text = '58000'

wyp_dod = SubElement(sam1,'wyposazenie_dod')

kolor = SubElement(wyp_dod,'kolor')
kolor.text = 'czarna perła'

klima = SubElement(wyp_dod,'klimatyzacja')
klima.text = 'DFE32454'


#drugi samochód
sam2 = SubElement(top,'samochod')

id = SubElement(sam2,'id')
id.text = 'sam2'

marka = SubElement(sam2,'marka')
marka.text = 'Subaru'

model = SubElement(sam2,'model')
model.text = 'Outback'

rok = SubElement(sam2,'rocznik')
rok.text = '2019'

poj = SubElement(sam2,'pojemnosc')
poj.text = '2.4'

cena = SubElement(sam2,'cena')
cena.text = '116000'

wyp_dod = SubElement(sam2,'wyposazenie_dod')

kolor = SubElement(wyp_dod,'kolor')
kolor.text = 'czerwony metaliic'

klima = SubElement(wyp_dod,'klimatyzacja')
klima.text = 'DWERDF4485938'

pod_po = SubElement(wyp_dod,'poduszki')
pod_po.text = '4'

print(pretty(top))

with open("subaru.xml","a",encoding="utf-8") as f:
    f.write(pretty(top))
