
Álgebra Abstracta - CCOMP3-2 // Permanente 02a
﻿# Generar-todos-los-primos-de-3-4-y-5-cifras.
 
Integrantes:

Fabricio Arian Messa Mandujano

Royer Diosdado Carcausto Choquehuanca


1.- Generar todos los primos de 3, 4 y 5 cifras.

Creamos una funcion que nos ayuda a generar numeros primos, luego creamos una lista entre el rango 2 hasta un numero x.

creamos un indice que empieza en 0 luego ira aumentando, luego creamos un while para no exceder el limite de x.

Creamos un for i in lista para recorrer la lista, seguido de un if i % lista[indice] == 0: si cada numero de toda la lista es divisible entre el indice,
entonces lo sacamos de la lista con lista.remove(i)

Aumentamos el indice con indice+=1, luego usamos return para que nos retorne la lista
    
Guardamos la variable y dependiendo de la canidad entra en un if, para:
if == 3 creamos un for para que vaya los primos mayores que 99
if == 4 creamos un for para que vaya los primos mayores que 999
if == 5 creamos un for para que vaya los primos mayores que 9999
