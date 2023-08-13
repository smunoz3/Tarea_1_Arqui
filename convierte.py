def int_to_binary(numero):
    es_negativo = False #(flag)
    entero = int(numero) #:V
    if entero <0:
        es_negativo= True
        entero = entero *-1
    decimal = round((numero - entero),10)
    lista_bin = []
    lista_bin_decimal = []
   
    while entero != 0:
        lista_bin.append(entero % 2)
        entero = entero // 2
    lista_bin.reverse()
    contador = 0
    temp = len(str(decimal))-1
    while contador < len(str(decimal))-1:
        if decimal == 0.0 or decimal == 1.0: #continuar
            break
        if (decimal*2.0 >= 1.0):
            lista_bin_decimal.append(1.0)
            decimal = decimal*2.0 - 1.0
        elif(decimal*2.0 < 1.0):
            lista_bin_decimal.append(0.0)
            decimal = decimal*2.0
        contador +=1
    if es_negativo == True:
        lista_bin = negacion_binary(lista_bin)
    lista_bin = lista_bin +lista_bin_decimal

def negacion_binary(lista):#resive array
    contador=0
    for i in lista:
        if int(i) == 0:
            lista[contador] = 1
        elif int(i) == 1:
            lista[contador] = 0
        contador +=1
    lista = suma_bin(lista,[1])
    return(lista)

def suma_bin(num1,num2):# mismo largo
    num1, num2=normalizacion_largo(num1,num2)
    num1.reverse()
    num2.reverse()
    num_fin =[]
    contador = 0
    carri = 0
    flag = True
    while contador<len(num1):
        if (int(num1[contador]) == 0)and(int(num1[contador]) == int(num2[contador])): #ambos 0
            if carri == 1:
                num_fin.append("0")
                carri = 0
            elif carri == 0:
                num_fin.append("0")
        elif (int(num1[contador]) == 1)and(int(num1[contador]) == int(num2[contador])): #ambos 1
            if carri == 1:
                num_fin.append("1")
                carri = 1
            elif carri == 0:
                num_fin.append("0")
                carri = 1
        else:
            if carri == 1:
                num_fin.append("0")
            elif carri == 0:
                num_fin.append("1")
        contador +=1
        if (contador == len(num1))and (flag ==True): # agrega uno de largo en array
            contador -=1
            flag = False
    num_fin.reverse()
    return num_fin

def normalizacion_largo(num_1,num_2):   #llegan como arrays
    if len(num_1)>=len(num_2):
        largo=len(num_1)
        i = len(num_2)
        num_2.reverse()
        while i < largo:
            num_2.append("0")
            i +=1
        num_2.reverse()
    elif len(num_1)<len(num_2):
        largo=len(num_2)
        i = len(num_1)
        num_1.reverse()
        while i < largo-1:  #probar
            num_1.append("0")
            i +=1
        num_1.reverse()
    return num_1,num_2
lista_1 =[0,1,0]
lista_2 =[0,1,1,9,9,0]

print(int_to_binary(47.5))
x,y =normalizacion_largo(lista_1,lista_2)

print(x)
print(y)