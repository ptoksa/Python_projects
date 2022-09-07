#Iän tarkistus
#ikä = int(input("Kerro ikäsi? "))
#if ikä < 0:
#    print(f"Taitaa olla virhe")
#elif ikä >= 0 and ikä <= 4:
#    print(f"En usko, että osaat kirjoittaa...")
#elif ikä >= 5:
#    print(f"Ok, olet siis {ikä}-vuotias")

#Veljenpojat
#nimi = input("Anna nimesi: ")
#if nimi == "Mortti" or nimi == "Vertti":
#    print(f"Olet luultavasti Mikki Hiiren veljenpoika.")
#elif nimi == "Hupu" or nimi == "Tupu" or nimi == "Lupu":
#    print(f"Olet luultavasti Aku Ankan veljenpoika.")
#else:
#    print(f"Et ole kenenkään tuntemani hahmon veljenpoika.")

#Arvosana ja pisteet
#pisteet = int(input("Anna pisteet [0-100]: "))
#if pisteet < 0:
#    print(f"mahdotonta!")
#if pisteet >= 0 and pisteet <= 49:
#    print(f"Arvosana: hylätty")
#if pisteet >= 50 and pisteet <= 59:
#    print(f"Arvosana: 1")
#if pisteet >= 60 and pisteet <= 69:
#    print(f"Arvosana: 2")
#if pisteet >= 70 and pisteet <= 79:
#    print(f"Arvosana: 3")
#if pisteet >= 80 and pisteet <= 89:
#    print(f"Arvosana: 4")
#if pisteet >= 90 and pisteet <= 100:
#    print(f"Arvosana: 5")
#if pisteet > 100:
#    print(f"mahdotonta!")

#FizzBuzz
#luku = int(input("Anna luku: "))
#if luku % 3 == 0 and luku % 5 == 0:
#    print(f"FizzBuzz")
#elif luku % 3 == 0:
#    print(f"Fizz")
#elif luku % 5 == 0:
#    print(f"Buzz")

#Karkausvuosi
vuosi = int(input("Anna vuosi: "))
if vuosi % 4 == 0 and (vuosi % 100 != 0 or vuosi % 400 == 0):
    print(f"Vuosi on karkausvuosi.")
else:
    print(f"Vuosi ei ole karkausvuosi.")


