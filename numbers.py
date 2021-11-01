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

if __name__ == "__main__":
    run()  

print("Eso es todo") 