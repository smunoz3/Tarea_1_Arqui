def int_to_binary(numero):
    '''
    recibe un int y lo trasnforma a binario, guardandolo en una lista 
    Retorna lista de numero en binario y si signo
    '''
    es_negativo = False #(flag)
    entero = int(numero) #:V
    if entero <0:
        es_negativo= True
        entero = entero *-1
    decimal = round((numero - entero),10)
    
    entero= entero_bin(entero)
    decimal= decimal_bin(decimal)
    entero.append('.')
    entero = entero + decimal
    return(entero,es_negativo)

def negacion_binary(lista):#resive array
    '''
    puede que no se use
    '''
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
    '''
    resive 2 int, llama a normalizacion_largo, 
    y cuando tienen el mismo largo los suma
    retorna una lista con el numero final en binario
    '''
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
    '''
    resive 2 numeros (listas) en binario y les iguala el largo
    # revisar posible que este mal
    retorna los 2 numeros con el mismo largo 
    '''
    num_1,pos_punto_inicial_1,orden_1 = modo_cientifico(num_1)
    num_2,pos_punto_inicial_2,orden_2 = modo_cientifico(num_2)
    if orden_1 == orden_2:
        return(num_1,num_2)
    elif orden_1>orden_2:
        #pos_punto_inicial_2 +=1
        if pos_punto_inicial_2 == -1:
            num_2.insert(-orden_1,'.')
            return(num_1,num_2)
        else:
            num_2.pop(pos_punto_inicial_2-1) #revisar
            num_2.insert(orden_1+1,'.')
            return(num_1,num_2)
    elif orden_1<orden_2:
        if pos_punto_inicial_1 == -1:
            num_1.insert(-orden_2,'.')
            return(num_1,num_2)
        else: #arreglar :v
            num_1.pop(pos_punto_inicial_1-orden_1) #revisar
            num_1.insert(orden_2,'.')
            return(num_1,num_2)



def binary_to_32bits(numero,es_negativo): #llega array , bool
    '''
    resive un numero en binario y si signo y lo construye en base 32 bits
    retorna el numero(lista) de 32bits
    '''
    numero,pos_punto_inicial,orden = modo_cientifico(numero)

    numero_final=[]
    if es_negativo == False:
        numero_final.append(0)
    else:
        numero_final.append(1)
    exponent,y = int_to_binary(127+ orden)
    exponent.remove('.')
    while len(exponent)<8:    #revisar
        exponent.insert(0,0)
    numero_final= numero_final +exponent

    mantissa = numero[pos_punto_inicial:]
    while len(mantissa)< 23:
        mantissa.append(0)
    numero_final =numero_final +mantissa
    return numero_final #return array len 32

def entero_bin(entero):
    '''
    trivial
    '''
    bin__entero = []
    while entero != 0:
        bin__entero.append(entero % 2)
        entero = entero // 2
    bin__entero.reverse()
    return bin__entero

def decimal_bin(decimal):
    '''
    trivial
    '''
    bin_decimal = []
    contador = 0
    limite = len(str(decimal))-1 #confirmar largo
    while contador < limite:
        if decimal == 0.0 or decimal == 1.0:
            break
        if (decimal*2.0 >= 1.0):
            bin_decimal.append(1)
            decimal = decimal*2.0 - 1.0
        elif(decimal*2.0 < 1.0):
            bin_decimal.append(0)
            decimal = decimal*2.0
        contador +=1
    return bin_decimal

def modo_cientifico(numero):
    '''
    resive un numero binario con punto (coma) y mueve el punto al primer uno de la izquierda
    retorna un numero (lista) con el punto despues del primer 1
    '''
    i = 0
    pos_punto_inicial = -1
    while i <len(numero):
        if numero[i] == '.':
            pos_punto_inicial = i
            break
        i += 1
    i = 0
    pos_primer_1 =-1
    while i <len(numero):
        if int(numero[i]) == 1:
            pos_primer_1 = i
            break
        i += 1
    orden = 0
    if pos_punto_inicial != -1:
        orden= pos_punto_inicial-pos_primer_1-1
        numero.pop(pos_punto_inicial)
        numero.insert(pos_primer_1+1,'.')
    return (numero,pos_punto_inicial,orden)

lista_1 =[0,1,0,0,'.',1,0,1,0,1,1]
lista_2 =[0,1,0,9,9,9,'.',2,9,9,9,9,9,2]
x,y =normalizacion_largo(lista_1,lista_2)

y = int_to_binary(54)
print(x)
print(y)