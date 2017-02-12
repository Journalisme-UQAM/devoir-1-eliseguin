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
