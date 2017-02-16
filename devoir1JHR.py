#coding:utf-8
permis1=list(range(30000,100000))
# print(permis1)
for permi1 in permis1:
    print(permi1)

permis2=list(range(0,18000))
for permi2 in permis2:
    if permi2<10: 
        print("0000{}".format(permi2))
    elif 100>permi2>=10:
        print("000{}".format(permi2))
    elif 1000>permi2>=100:
        print("00{}".format(permi2))
    elif 10000>permi2>=1000:
        print("0{}".format(permi2))
    else:
        print("{}".format(permi2))

# Solution intéressante!
# Tu t'es servie des conditions. Super!
# Il aurait été possible de le faire plus simplement, cependant.
# Voici ma proposition:

for p2 in range(0,18000):
    if p2 < 10:
        print("0000{}".format(p2))
    elif p2 < 100: # Il n'est pas nécessaire de vérifier, ici, si le nombre est plus grand que 10, car la condition précédente fait justement cette vérification
        print("000{}".format(p2))
    elif p2 < 1000:
        print("00{}".format(p2))
    elif p2 < 10000:
        print("0{}".format(p2))
    else:
        print(p2)