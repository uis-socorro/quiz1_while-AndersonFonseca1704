print("------------------------------")
print("----------NEGOCIO-------------")
print("------------------------------")


c1 =int(input("digite el capital de pedro"))
c2 =int(input("digite el capital de juan"))
c3 =int(input("digite el capital a invertir"))
c4=0
i=0
#processing

while c4<=c3:
  c1=(c1*0.03)+c1
  c2=(c2*0.04)+c2
  c4=c1+c2
  i+=1

#ouput
  
print("en ",i," meses pedro y Juan tendrán ",c4," pesos y podrán crear el negocio")