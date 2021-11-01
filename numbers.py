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


for i in range(-1,51,2):
    if i > 0:
        print(f"numero impar {i}")
      
     

if __name__ == "__main__":
    run()  

print("Eso es todo") 