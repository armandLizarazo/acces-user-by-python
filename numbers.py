end = "End Program"
def run():
  tabla = int(input("Que tabla quiere consultar? "))
  i = 1

  while i <= 10:
      print (str(tabla) +" x " + str(i) + " = " + str(tabla * i))
      i += 1

for i in range(0,5):
    print ("hola numero de x es ...", i)




if __name__ == "__main__":
    run()  

print(end) 