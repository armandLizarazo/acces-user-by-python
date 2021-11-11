

def verify_number ():
  character_count = len(contact)
  if character_count != 10:
    print(f"Vaya! {contact} no es un numero de contacto valido.")
    if character_count > 10:
      print(f"ingresaste {character_count -10} numero(s) de mas.")
    else:
      print(f"al parecer te faltaron {10 - character_count} digitos.")
    if (character_count < 3000000000 or character_count > 3509999999):
      print("Numero de contacto no valido")       
  else:
    user1 = [name, last_name, contact]
    print(user1)
    print(f"""
Registro exitoso! 
Usuario: usuario1
Nombre: {name} {last_name}
Edad: {age} años
Numero de contacto: {contact}
""")
    

name = 0
last_name = 0
contact = 0

name = input("Escribe tu nombre: ").capitalize()
last_name = input("Escribe tu apellido: ").capitalize()
age = 2021 - int(input("Año de nacimiento "))
if (age < 13 or age > 150):
  print(f"Edad: {age} años")
  print("No estas en edad para entrar aqui.")
  exit()  
contact = input("Numero de celular: ")
verify_number()




