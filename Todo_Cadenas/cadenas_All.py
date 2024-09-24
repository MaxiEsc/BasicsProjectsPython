# Manejo de cadenas en Python

cadena_1 = "Hola a todos"
cadena_1 = "Adios"
cadema_2 = "es Interesante"
cadena_3 = '''este es un ejemplo de multiples lineas en
    en una cadena y es interesante es ta 
        funcionalidad'''
print(cadena_1)
print(cadema_2)
print(cadena_3)

# Indices de una cadena en detalle como si fuera un arreglo como si fuera un indice i
print("Indices de una cadena en detalle como si fuera un arreglo como si fuera un indice i")
cadena_a = 'Hola mundo'
print(cadena_a)

primer_caracter = cadena_a[0]
print(primer_caracter)
ultimo_caracter = cadena_a[9]
print(ultimo_caracter)

#inmutabilidad de una cadena... En teoria la idea de este concepto es que tras la creacion de una cadena en teoria
# los caracter dentro de la misma no pueden ser modificados.
# en caso de quere mpdificarlo eeta de crear una nueva cadena con los caracteres
cadena_1 = 'Hola Mundo'
#cadena_1[0] = J // no se puede asignar de esta manera la maodificacion correspondente por que ya esta apuntando a un objeto
cadena_1 = 'Adios'
#caracteres especiales como '\n, \t, \',  el cual son el enter tabulacion,  y ' como tambien \\ y \''
print("Hola \n mundo")
print("es interesante como se \t llevan la idea entre \\ \''los lenguajes\''")
#Concatenacion de cadenas uso del operador +, como tambien tenemos el metodo como el metodo Join.
print("Hola " + "mundo")
prueba = '\n\n\n-----------------------------------\n\n\n\n'.join([cadena_1,cadema_2,cadena_3,cadena_a])
print(prueba)

#Formato de cadenas como opciones de formateo permite usar el fstring es la idea como f' hola {$variable}
# tambien disponemos del antiguo metodo format como resultado = 'Hola {}'.format($variable)

#Formateo de cadenas
nombre = 'Juan'
edad = 30
# con fstring
mensaje = f'Hola me llamo {nombre} y tengo {edad} años'
print(mensaje)
#Con metodo format
mensaje = 'Hola, me llamo {} y tengo {} años.'.format(nombre,edad)
print(mensaje)
cadena_1 = '   saludos a todos los saludadores   '
#Metodos en las cadenas upper() mayusculas, lower() minusculas, spli() quitar espacios().
print("Cadena original mayusculas: {}".format(cadena_1).upper())
print("Cadena original minusculas: {}" .format(cadena_1).lower())
print("Cadena original sin espacios: {}" .format(cadena_1.strip()))
#con fprint
print(f"Cadena original mayusculas: {cadena_1.upper()}")
print(f"Cadena original minusculas: {cadena_1.lower()}")
print(f"Cadena original sin espacios: {cadena_1.strip()}")

#Funcion Len() ver el largo de una cadena.
cadena = "Hola,  mundo!"
largo_cadena = len(cadena)
print(f'cadena original: {cadena}')
print(f'largo de cadena original: {len(cadena)}')
#Sub cadenas en pyhon (slicing) este conceptopermite la estraccion de cadenas
#Manejo de subcadenas.
cadena = "Hola,  mundo!"
subacadena_hola = cadena[0:4]
print(f"subcadena de hola {subacadena_hola}")
subacadena_mundo = cadena[7:12]
print(f"subcadena de mundo {subacadena_mundo}")
# como buscar las subcadenas con find()
cadena = "Hola,  mundo!"
indice = cadena.find("mundo")
print(f'indice de la subcadena mundo: {indice}')
indice = cadena.find("Hola")
print(f'indice de la subcadena mundo: {indice}')
#Reemplazo de cadenas de python con el metodo replace()
#En este caso lo que hace el metodo es reemplazo
cadena = "Hola,  mundo!"
reemplazar_subacadenas = cadena.replace('mundo', 'a todos')
print(f'Nueva cadena reemplazada: {reemplazar_subacadenas}')
reemplazar_subacadenas = cadena.replace('Hola', 'adios ')
print(f'Nueva cadena reemplazada: {reemplazar_subacadenas}')
#Separar subacadenas
# Con el metodo split(',') se va a separar las cadenas en las condiciones mas necesarias
cadena = "Hola,  mundo!"
lista_de_Separacion = cadena.split(' ')
print(lista_de_Separacion)
prueba= 'negro,jose'
lista_de_Separacion = prueba.split(',')
print(lista_de_Separacion)
# Multiplicacion de cadenas.
#resultado = texto * veces

repetir = 7
cadena = "Hola,  mundo!"

resultado = cadena * repetir
print(resultado)

#Ejercicio  de mail.
print('-' * 1000)
nombre = 'Doctor Sanada Akihiko'
empresa = 'Soluciones Corporativas'
dominio = 'com.ar'

print('Nombre: {} \nEmpresa: {}\nDominio: {}'.format(nombre,empresa,dominio))
nombre = 'Doctor Sanada Akihiko'.split(" ")
empresa = 'Soluciones Corporativas'.split(" ")

email =  nombre[0].lower() + "." + nombre[1].lower() + "." + nombre[2].lower() + "@" + empresa[0].lower() + empresa[1].lower() + "." + dominio

print(email)