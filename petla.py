print("Podaj kwotę początkową pożyczki: ")
kwota_pozyczki = round(float(input()),2)
print("Podaj wsysokość raty: ")
kwota_raty = round(float(input()),2)
print("Podaj oprocentowanie kredytu: ")
oprocentowanie = float(input())

tmp = "Twoja pozostała kwota kredytu to {} złotych, to {} mniej niż w poprzednim miesiącu"
tmp_2 = "Kwota początkowa kredytu to {} złotych, rata wynosi {} złotych, a oprocentowanie to {} %"

print(tmp_2.format(kwota_pozyczki,kwota_raty,oprocentowanie))

plik = open("inflacja.txt","r")

lista = []
for line in plik:
    lista.append(line.strip())
plik.close()

a=len(lista)
i=0
while i<a:
    inflacja = float(lista[i])
    pozostało = round((1 + ((inflacja + oprocentowanie) / 1200)) * kwota_pozyczki - 200, 2)
    roznica = round(kwota_pozyczki - pozostało, 2)
    print(tmp.format(pozostało, roznica))
    kwota_pozyczki = pozostało
    i += 1
