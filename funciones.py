usuario_1 = ['Armando', 'Lizarazo', 43, 1.68]
usuario_2 = ['Luis', 'Ramirez', 21, 1.69]
usuario_3 = ['Diego', 'Linares', 15, 1.65]
usuario_4 = ['Marcela', 'Castro', 18, 1.62]
usuario_5 = []
bienvenida = '  Felicidades!!  '
despedida = '   Estas dentro  '
nombre = 0
apellido = 0
edad = 0
estatura = 0


print('''
Bienvenid@ mi Programa
Primero debes identificarte,
Recuerda que debes ser mayor de edad para ser admitid@.
''')

identificacion = input('Ingresa tu codigo de usuario...')

print (identificacion)

if (identificacion == usuario_1):
  print (identificacion.capitalize())
else:
  print('Wtf dyw?...')

usuario = input('digita tu nombre ')
usuario = usuario.capitalize()


if (usuario == usuario_1[0]):
  edad = usuario_1[2]
elif (usuario == usuario_2[0]):
  edad = usuario_2[2]
elif (usuario == usuario_3[0]):
  edad = usuario_3[2]
elif (usuario == usuario_4[0]):
  edad = usuario_4[2]
 
print(edad)

if (edad == 0):
  bienvenida = "'...i'm SORRY..."
  despedida = "  Ponte en contacto con el Administrador 304 631 3114  "
elif (edad < 18):
  bienvenida = "Lo sentimos..."
  despedida = "  bye!  "



def registro():  
  print("Dejanos tu informacion")
  nombre = input("nombre: ").capitalize()
  apellido = input("apellido: ").capitalize()
  nacimiento = int(input("año de nacimiento: "))
  edad = 2021 - nacimiento 
  estatura = input("estatura: ")
  celular = input("Numero de contacto ")
  validacion = len(celular)
  if validacion != 10:
    print("Numero de celular no valido")
    celular = input("Numero de contacto: ")
    validacion = len(celular)
    if validacion != 10:
      print("Numero de celular no valido")
      print(f"error: {validacion} deseas intentarlo nuevamente?")
      opcion = input(("""
      y-Si
      n-No
          """))
      opcion = opcion
      y = "y"
      n = "n"
      if opcion == y:
        registro()
      else:
        print(bienvenida)
  else:
    # celular = celular
    print (f"Tu nombre es {nombre} {apellido}, tienes {edad} años y mides {estatura} es correcto?" )
    opcion = input(("""
    y-Si
    n-No
        """))
    opcion = opcion
    y = "y"
    n = "n"
    if opcion == y:
      print(f"{nombre} pronto recibiras un mensaje de texto con tu usuario o...")
    elif opcion == n:
      print("Intenta nuevamente...")
      registro() 

      
def autorized ():
  if edad >= 18:   
    print (f'{usuario}, tienes {edad} años, bienvenid@.')
  elif edad == 0:
    print (f'{usuario}, no existes en nuestra base de datos, deseas registrarte?')
    respuesta = int(input("""
    1-Si
    2-No
    """))
    if (respuesta == 1):
      registro() 
    elif(respuesta == 2):
      print('Hasta luego...')
  else:
    print (f'{usuario}, tienes {edad} años, no eres mayor edad, no puedes entrar.')



print (bienvenida.center(60, '='))
autorized()
print (despedida.center(60, '='))

