def generar_primo(numero): #funcion para generar primos
    lista = list(range(2, numero + 1)) #creo una lista entre el rango 2 hasta un número "x"
    indice = 0 #el indice empezará en 0, y luego lo iremos aumentando 
    while lista[indice]**2 <= numero: #esto es para que no exceda el límite del número "x" y aparte es para romper el ciclo while
        for i in lista: #recorremos la lista
            if i % lista[indice] == 0: #si cada número de toda la lista es divisible entre el índice entonces lo sacamos de la lista
                lista.remove(i)
        indice += 1 #aumentamos el ínidce 
    return lista #retornamos la lista

print("Generar todos los primos de 3, 4 y 5 cifras")
cantidad = int(input("Escoja la cantidad de cifras que quiere: ")) #se guarda la variable y dependiendo de la cantidad entra en un if
if cantidad == 3:
    print("Todos los primos de 3 cifras")
    primos1 = generar_primo(999)
    for i in primos1: #éste for es para imprimir solo los primos mayores que 99
        if i > 99:
            print(i)
if cantidad == 4:
    print("Todos los primos de 4 cifras")
    primos2 = generar_primo(9999)
    for i in primos2: #éste para los primos mayores a 999
        if i > 999:
            print(i)
if cantidad == 5:
    print("Todos los primos de 5 cifras")
    primos3 = generar_primo(99999)
    for i in primos3: #éste para los primos mayores a 9999
        if i > 9999:
            print(i)



