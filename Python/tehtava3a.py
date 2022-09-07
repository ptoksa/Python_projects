# Määritellään funktio
def testifunktio():
    print('Terveiset testifuntiosta')
# Luodaan funktio, joka saa parametrina toisen funktion
def aja_funktio(funktio):
# Kutsutaan parametrina annettua funktiota aja_funktio:n sisällä
    funktio()
# Nyt aja_funtion sisällä kutsutaan testifunktiota
aja_funktio(testifunktio) # Tulostuu 'Terveiset testifunktiosta'
