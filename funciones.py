

usuario1 = ['Armando', 'Lizarazo', 43, 1.68]
usuario2 = ['Luis', 'Ramirez', 21, 1.69]
usuario3 = ['Diego', 'Linares', 15, 1.65]
usuario4 = ['Marcela', 'Castro', 18, 1.62]
usuario5 = []
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

if (identificacion == usuario1):
  print (identificacion.capitalize())
else:
  print('Wtf dyw?...')

usuario = input('digita tu nombre ')
usuario = usuario.capitalize()


if (usuario == usuario1[0]):
  edad = usuario1[2]
elif (usuario == usuario2[0]):
  edad = usuario2[2]
elif (usuario == usuario3[0]):
  edad = usuario3[2]
elif (usuario == usuario4[0]):
  edad = usuario4[2]
 
print(edad)

if (edad == 0):
  bienvenida = "'...i'm SORRY..."
  despedida = "  Ponte en contacto con el Administrador 304 631 3114  "
elif (edad < 18):
  bienvenida = "Lo sentimos..."
  despedida = "  anda... a Crecer!  "

answer1 = 0





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
      print("Dejanos tu numero y nos pondremos en contacto")
      input()
      print('Hasta Luego')
    elif(respuesta == 2):
      print('Hasta luego...')
  else:
    print (f'{usuario}, tienes {edad} años, no eres mayor edad, no puedes entrar.')



print (bienvenida.center(60, '='))
autorized()
print (despedida.center(60, '='))

