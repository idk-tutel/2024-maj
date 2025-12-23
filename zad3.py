#3.1


def funkcja(n):#Efiszensi
    i = 1
    w = 0
    while i == 1:
        if n < 10:
            i =0
        if n % 2 == 0:
            while n % 10 != 0:
                n -= 2
            n /= 10
        else:
            while n % 10 != 0:
                n -= 1
                w+=1
            w*=10
            n /= 10
    n = w
    i = 1
    w = 0
    while i == 1:
        if n < 10:
            i = 0
        if n % 2 == 0:
            while n % 10 != 0:
                n -= 2
            n /= 10
        else:
            while n % 10 != 0:
                n -= 1
                w += 1
            w *= 10
            n /= 10
    return w//10
print(funkcja(512443652357))
print(funkcja(10409))
print(funkcja(6))
#3.2        Odp: ilosc=18, max=28422
cos = open("Dane/skrot.txt", "r").read()
cos = cos.split()
w, maxcos=0,0
for i in cos:
    i = int(i)
    if funkcja(i)==0:
        w+=1
        if i >=maxcos:
            maxcos=i
print("")
print(w)
print(maxcos)
print("")
#3.3         ODP!!!::: 784, 14196, 2247, 24087, 3871, 10192
cos = open("Dane/skrot2.txt", "r").read()
cos = cos.split()
w=[]
for i in cos:
    i = int(i)
    e = 0
    for stupid in range(i-1):#to jest takie szybkie
        stupid+=1
        if funkcja(i)%stupid==0 and i%stupid==0:
            if stupid == 7 or stupid == i or stupid == funkcja(i):
                if stupid == 7:
                    e = -1
            else:
                e = 1
    if e == -1:
        w.append(i)
print(w)