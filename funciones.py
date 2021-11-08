

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
  despedida = "  anda... a Crecer!  "

answer_1 = 0



contacto = 0

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
      print("Dejanos tu informacion")
      nombre = input("Nombre: ")
      apellido = input("apellido: ")
      nacimiento = input("año de nacimiento: ")
      estatura = input("estatura: ")
      print('Hasta Luego')
      print (f"Tu nombre es {nombre} {apellido}, naciste en {nacimiento}, mides {estatura} es correcto?" )
    elif(respuesta == 2):
      print('Hasta luego...')
  else:
    print (f'{usuario}, tienes {edad} años, no eres mayor edad, no puedes entrar.')



print (bienvenida.center(60, '='))
autorized()
print (despedida.center(60, '='))

