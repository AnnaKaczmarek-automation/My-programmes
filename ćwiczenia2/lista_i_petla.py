owoce=['arbuz', 'banan', 'cytryna', 'granat', 'porzeczka']
print(owoce)
odpowiedz=input("Czy chcesz wyświetlić nazwy owoców w kolejności alfabetycznej? Wpisz tak lub nie: ")
print(odpowiedz)
t='tak'
n='nie'
while odpowiedz != "exit":
    if odpowiedz == t :
        print(owoce)
        break
    elif odpowiedz == n :
        owoce.reverse()
        print(owoce)
        break
    else:
        print("Nie odpowiedziałeś zgodnie z pytaniem")
        print(odpowiedz)
        odpowiedz=input("Czy chcesz wyświetlić nazwy owoców w kolejności alfabetycznej? Wpisz tak lub nie: ")

print("program zakończony")

