#4.1      ODP:!::!:!::212
lol = open("Dane/liczby_przyklad.txt", "r").read()
wiersz1 = lol.split("\n")[0].split(" ")
wiersz2 = lol.split("\n")[1].split(" ")
w = 0
for i in wiersz1:
    for j in wiersz2:
        if int(j)%int(i)==0:
            w+=1
            break
print(w)
print(wiersz1)
print(wiersz2)
#4.2          ODDPD::31
for i in range(len(wiersz1)):
    wiersz1[i] = int(wiersz1[i])
wiersz1.sort()
print(wiersz1[100])
print(wiersz1[101])
print(wiersz1[102])
#4.3          ODP:::547839600, 2954285, 573219169, 573549984, 212444924
for i in range(len(wiersz2)):
    wiersz2[i] = int(wiersz2[i])
lista = {}
for i in range(len(wiersz1)-1):
    if wiersz1[i] not in lista:
        lista[wiersz1[i]] = 0
    lista[wiersz1[i]] += 1
print(lista)
for num in wiersz2:
    tnum = num
    liczby = []
    templista = lista.copy()
    for i in templista:
        for j in range(templista[i]):
            if num%i==0:
                num/=i
                liczby.append(i)
            else: break
    if num ==1:
        print(tnum)
#4.4            help.
wiersz1 = lol.split("\n")[0].split(" ")
for i in range(len(wiersz1)):
    wiersz1[i] = int(wiersz1[i])
w = [0, 0, 0]
for i in range(len(wiersz1)-50):
    srednia = sum(wiersz1[i:i+50])/50
    j=1
    while True:
        if len(wiersz1) >= i+j and srednia < sum(wiersz1[i:i+j])/(49+j):
            srednia = sum(wiersz1[i:i+j])/(49+j)
        else:
            break
        j+=1
    if srednia > w[0]:
        w[0] = srednia
        w[1] = j+49
        w[2] = i
print(w)