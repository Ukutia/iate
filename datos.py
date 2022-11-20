ea = "aaa"
import random
datos = open("base.txt","w")
a = 0
tre = ""
tre2 = ""
e = 0
list = [18,19,20,21,22]
list2 = [0,1,2,3,4,5,6,7,8,9]
while(a < 100):
    e = 0
    while(e < 3):
        tre += str(random.choice(list2))
        tre2 += str(random.choice(list2))
        e += 1
    txt = str(random.choice(list))+"."+str(tre)+"."+str(tre2)+"-"+str(random.choice(list2))+"  Numero de Almuerzos: "+str(random.choice(list2))+"\n"
    print(txt)
    datos.write(txt)
    tre = ""
    tre2 = ""
    a += 1