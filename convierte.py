def int_to_binary(numero):
    '''
    recibe un int y lo trasnforma a binario, guardandolo en una lista
    Retorna lista de numero en binario y si signo
    '''
    es_negativo = False #(flag)
    numero = float(numero)
    entero = int(numero) #:V
    if entero <0:
        es_negativo= True
        entero = entero *-1
    decimal = round((numero - entero),10)
   
    entero= entero_bin(entero)
    decimal= decimal_bin(decimal,len(entero)-1)
    entero.append('.')
    entero = entero + decimal
    return(entero,es_negativo)

def igualacion_de_largos(num1,num2):
    punto1 = -1
    punto2 = -1
    i = 0
    while True:
        try: 
            if num1[i] == '.':
                punto1 = i
        except IndexError:
            i = i
        try: 
            if num2[i] == '.':
                punto2 = i
        except IndexError:
            i = i
        i += 1
        if (punto1 != -1) and (punto2!=-1):
            break 
    
    #Antes punto
    if punto1 > punto2:
        while punto2 != punto1:
            num2.insert(0,0)
            punto2 += 1
    elif punto1 < punto2:
        while punto2 != punto1:
            num1.insert(0,0)
            punto1 += 1

    #Despues punto
    n_despues_1 = len(num1) - punto1
    n_despues_2 = len(num2) - punto2
    if n_despues_1 > n_despues_2:
        while n_despues_1 != n_despues_2:
            num2.insert(-1,0)
            n_despues_2 += 1
    elif n_despues_1 < n_despues_2:
        while n_despues_1 != n_despues_2:
            num1.insert(-1,0)
            n_despues_1 += 1
    
    return num1, num2, punto1

    print(punto1,punto2)
    # largo_mayor_antes_punto = 0
    # largo_mayor_despues_punto = 0
    # paso_por_punto = False
    # i = 0
    # veces_punto = 0
    # while (i < len(num1)) and (i < len(num2)):
    #     if paso_por_punto == False:
    #         largo_mayor_antes_punto += 1
    #         try:
    #             num1[i]
    #         except IndexError:
    #             mayor_antes_punto = num2
    #         try:
    #             num2[i]
    #         except IndexError:
    #             mayor_antes_punto = num1


    #     if num1[i] == '.' or num2[i] == '.':
    #         if num1[i] == num2[i]:
    #             paso_por_punto = True
    #         elif veces_punto == 1:
    #             paso_por_punto = True
    #         veces_punto +=1
        
    #     if paso_por_punto:
    #         largo_mayor_despues_punto += 1
        
    #     i += 1

def suma_bin(num1,num2):# mismo largo
    '''
    resive 2 listas de binario, llama a normalizacion_largo,
    y cuando tienen el mismo largo los suma
    retorna una lista con el numero final en binario
    '''
    signo = num1[0]
    if signo == 0:
        signo = False
    elif signo == 1:
        signo = True
    exponente1 = num1[1:9]
    exponente1 = binary_to_int(exponente1)  #Exponente esta en int
    mantissa1 = num1[9:]

    mantissa1.insert(0,'.')
    mantissa1.insert(0,1)

    exponente2 = num2[1:9]
    exponente2 = binary_to_int(exponente2)  #Exponente esta en int

    mantissa2 = num2[9:]

    mantissa2.insert(0,'.')
    mantissa2.insert(0,1)

    shift = exponente1 - exponente2
    if shift < 0:
        i = 0
        while i != shift:
            mantissa1.pop(i+1)
            mantissa1.insert(i+2,'.')
            i += 1
        orden = exponente2 - 127

    elif shift > 0:
        i = 0
        while i != shift:
            mantissa2.pop(i+1)
            mantissa2.insert(i+2,'.')
            i += 1
        orden = exponente1 - 127
        
    
    # num1, num2, orden =normalizacion_largo(num1,num2)
    # num1,num2, orden = igualacion_de_largos(num1,num2)

    mantissa1.remove('.')
    mantissa2.remove('.')
    mantissa1.reverse()
    mantissa2.reverse()
    suma =[]
    contador = 0
    carri = 0
    #flag = True

    while contador<len(mantissa1):
        if (mantissa1[contador] == 0)and(mantissa1[contador] == mantissa2[contador]): #ambos 0
            if carri == 1:
                suma.append(1)
                carri = 0
            elif carri == 0:
                suma.append(0)
        elif (mantissa1[contador] == 1)and(mantissa1[contador] == mantissa2[contador]): #ambos 1
            if carri == 1:
                suma.append(1)
            elif carri == 0:
                suma.append(0)
                carri = 1
        else:
            if carri == 1:
                suma.append(0)
            elif carri == 0:
                suma.append(1)
        contador +=1
        # if (contador == len(num1))and (flag ==True): # agrega uno de largo en array
        #     contador -=1
        #     flag = False
    suma.reverse()
    suma.insert(orden,'.')

    suma,pos_primer_1,pos_punto_inicial,mov_punto = modo_cientifico(suma)
    orden += mov_punto

    return suma,orden

def sum_to_32bits(numero,orden,es_negativo):

    numero_final=[]
    if es_negativo == False:
        numero_final.append(0)
    else:
        numero_final.append(1)
    exponent,y = int_to_binary(127+ orden)
    exponent.remove('.')
    while len(exponent)<8:    #revisar
        exponent.insert(0,0)
    numero_final= numero_final + exponent

    i = 0
    pos_punto = 0
    while i < len(numero):
        if numero[i] == '.':
            pos_punto = i
            break
        i += 1

    mantissa = numero[pos_punto:]
    while len(mantissa)< 23:
        mantissa.append(0)
    numero_final =numero_final +mantissa
    return numero_final #return array len 32


def normalizacion_largo(num_1,num_2):   #llegan como arrays
    '''
    resive 2 numeros (listas) en binario y les iguala el orden
    # revisar posible que este mal
    retorna los 2 numeros con el mismo largo
    '''
    num_1,pos_primer_1_1,pos_punto_inicial_1,orden_1 = modo_cientifico(num_1)
    num_2,pos_primer_1_2,pos_punto_inicial_2,orden_2 = modo_cientifico(num_2)
    if orden_1 == orden_2:
        return(num_1,num_2,orden_2)
   
    #Se llega al orden de 1
    elif orden_1>orden_2:
        #pos_punto_inicial_2 +=1
        if pos_punto_inicial_2 == -1:
            num_2.insert(-orden_1,'.')
            return(num_1,num_2,orden_1)
        else:
            num_1.pop(pos_primer_1_1+1) #revisar
            num_1.insert(pos_primer_1_1 + 1 + (orden_1-orden_2),'.')
            return(num_1,num_2,orden_2)
        '''
        try:
            text[i+1]
        except IndexError:
            return False
        '''
    #Se llega al orden de 2
    elif orden_1<orden_2:
        if pos_punto_inicial_1 == -1:
            num_1.insert(-orden_2,'.')
            return(num_1,num_2,orden_2)
        else: 
            num_2.pop(pos_primer_1_2+1) #revisar
            num_2.insert(pos_primer_1_2 + 1 + (orden_2-orden_1),'.')
            return(num_1,num_2,orden_1)

def binary_to_32bits(numero,es_negativo): #llega array , bool
    '''
    resive un numero en binario y si signo y lo construye en base 32 bits
    retorna el numero(lista) de 32bits
    '''
    numero,pos_primer_1,pos_punto_inicial,orden = modo_cientifico(numero)

    numero_final=[]
    if es_negativo == False:
        numero_final.append(0)
    else:
        numero_final.append(1)
    exponent,y = int_to_binary(127+ orden)
    exponent.remove('.')
    while len(exponent)<8:    #revisar
        exponent.insert(0,0)
    numero_final= numero_final + exponent

    mantissa = numero[pos_primer_1+2:]
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

def decimal_bin(decimal,limite):
    '''
    trivial
    '''
    bin_decimal = []
    contador = 0
    while contador < (23 - limite):
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
        if numero[i] == 1:
            pos_primer_1 = i
            break
        i += 1
    orden = 0
    if pos_punto_inicial != -1:
        if pos_punto_inicial > pos_primer_1:
            orden= pos_punto_inicial-pos_primer_1-1
            numero.pop(pos_punto_inicial)
            numero.insert(pos_primer_1+1,'.')

        elif pos_punto_inicial < pos_primer_1:
            orden= pos_punto_inicial-pos_primer_1
            numero.pop(pos_punto_inicial)
            numero.insert(pos_primer_1,'.')
            
    return (numero,pos_primer_1,pos_punto_inicial,orden)

def binary_to_int(binario):
    binario.reverse()
    i = 0
    decimal = 0
    while i < len(binario):
        decimal += binario[i]*(2**i)
        i += 1
    return decimal


with open("operaciones.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.split(';')

    #Numeros en binario
        num1,sig1 = int_to_binary(linea[0])
        num2,sig2 = int_to_binary(linea[1])

        bin1 = binary_to_32bits(num1,sig1)
        bin2 = binary_to_32bits(num2,sig2)

        if sig1 != sig2:
            bin1 = "".join([str(elemento) for elemento in bin1])
            bin2 = "".join([str(elemento) for elemento in bin2])
            with open("resultados.txt" , "a") as arch_resultados:
                arch_resultados.write(linea[0]+'/'+bin1+';'+linea[1]+'/'+bin2+'\n')
        else:
            suma,orden = suma_bin(bin1,bin2)
            resultado = sum_to_32bits(suma,orden,sig1)
            resultado = "".join([str(elemento) for elemento in resultado])
            with open("resultados.txt" , "a") as arch_resultados:
                arch_resultados.write(resultado+'/'+'resultado_bin_32'+'\n')
