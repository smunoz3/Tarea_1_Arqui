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

def suma_bin(num1,num2):# mismo largo
    '''
    resive 2 listas de binario, llama a ,
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
        while i != abs(shift):
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
    
    mantissa1.remove('.')
    mantissa2.remove('.')
    mantissa1.reverse()
    mantissa2.reverse()


    suma =[]
    contador = 0
    carri = 0

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
    
    suma.reverse()
    suma.insert(orden,'.')

    suma,pos_primer_1,mov_punto = modo_cientifico(suma)
    orden += mov_punto

    return suma,orden

def binary_to_32bits(numero): #llega array
    '''
    resive un numero lo pasa a binario luego a base 32 bits
    retorna el numero(lista) de 32bits
    '''
    numero,signo = int_to_binary(numero)
    numero,pos_primer_1,orden = modo_cientifico(numero)

    numero_final=[]
    if signo == False:
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
            
    return (numero,pos_primer_1,orden)

def binary_to_int(binario):
    binario.reverse()
    i = 0
    decimal = 0
    while i < len(binario):
        decimal += binario[i]*(2**i)
        i += 1
    return decimal


#main()
lineas_totales = 0
lineas_sum = 0
lineas_no_sum = 0
with open("operaciones.txt", "r") as archivo:
    for linea in archivo:
        lineas_totales +=1
        linea = linea.split(';')

        bin1 = binary_to_32bits(linea[0])
        bin2 = binary_to_32bits(linea[1])

        if bin1[0] != bin2[0]:
            lineas_no_sum += 1
            bin1 = "".join([str(elemento) for elemento in bin1])
            bin2 = "".join([str(elemento) for elemento in bin2])
            with open("resultados.txt" , "a") as arch_resultados:
                arch_resultados.write(linea[0]+'/'+bin1+';'+linea[1]+'/'+bin2+'\n')
        else:
            lineas_sum +=1
            suma,orden = suma_bin(bin1,bin2)
            resultado = sum_to_32bits(suma,orden,bin1[0])
            resultado = "".join([str(elemento) for elemento in resultado])
            with open("resultados.txt" , "a") as arch_resultados:
                arch_resultados.write(resultado+'/'+'resultado_bin_32'+'\n')