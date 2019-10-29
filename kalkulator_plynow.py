print('''Witamy w kalkulatorze wody!!!!!
Dzięki tej aplikacji możesz łatwo i szybko
obliczyć swoje zapotrzebowanie na wodę
w zależności od tego ile wypiłaś/eś filiżanek kawy''')
print()
print()
kawa = input("Podaj ile wypiłeś już filiżanek kawy: ")
print("Liczba wypitych filiżanek kawy to: "+ kawa) 
print ("Sprawdźmy ile powinienieś wypić dzisiaj szklanek wody: ")

woda= int(kawa)*2+10
print(woda)


if int(kawa) <= 4:
    print("Wszystko jest dobrze.Nie przekroczyłeś bezpiecznej dawki kofeiny")
else:
    print("Uwaga! Wypiłeś bardzo dużo kawy. W miare możliwości połóż się spać")
