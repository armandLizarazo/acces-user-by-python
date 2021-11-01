import locale
def run():
  tabla = int(input(
"""
====================
Bienvenido al programa de tablas...
Que tabla quiere consultar? """))
  i = 1
  while i <= 10:
      print (str(tabla) +" x " + str(i) + " = " + str(tabla * i))
      i += 1

i = round(float(input(
    """
Bienvenido al programa consulta de numeros pares e impares...
por favor digite el numero a consultar... 
""")))
# for i in range(1, 50):
if (i % 2 != 0):
    print(f"El numero {i} es numero impar")
else:
    print(f"El numero {i} es numero par")
            
      
     

if __name__ == "__main__":
    run()  

print("Eso es todo") 