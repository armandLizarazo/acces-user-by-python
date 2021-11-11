

def autenticar_contacto ():
  cont = len(contacto)
  if cont != 10:
    print(f"Vaya! {contacto} no es un numero de contacto valido.")
    if cont > 10:
      print(f"ingresaste {cont -10} numero(s) de mas.")
    else:
      print(f"al parecer te faltaron {10 - cont} digitos.")
    if (cont < 3000000000 or cont > 3509999999):
      print("Numero de contacto no valido")       
  else:
    usuario1 = [nombre, apellido, contacto]
    print(usuario1)
    print(f"""
Registro exitoso! 
Usuario: usuario1
Nombre: {nombre} {apellido}
Edad: {edad} años
Numero de contacto: {contacto}
""")
    

nombre = 0
apellido = 0
contacto = 0

nombre = input("Escribe tu nombre: ").capitalize()
apellido = input("Escribe tu apellido: ").capitalize()
edad = 2021 - int(input("Año de nacimiento "))
if (edad < 13 or edad > 150):
  print(f"Edad: {edad} años")
  print("No estas en edad para entrar aqui.")
  exit()  
contacto = input("Numero de celular: ")
autenticar_contacto()




