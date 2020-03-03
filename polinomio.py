def polinomio(x,poli):
    y = 0
    a  = len(poli)-1  
    for i in range(0,len(poli)):     
        y+= poli[i]*pow(x,a)
        a -= 1
    return y




def gerarpolinomio(grau):
    poli = []
    flag = True
    flag2 = False
    while flag:
        lista = input("Insira os coeficientes, separados por vírgulas(,) >> " )      
        cont = lista.count(',')
        if (cont != (grau)):
            print("Entrada inválida, por favor confira os valores e digite novamente")
        else:
            
            for i in lista:
                if (((ord(i)>75)or(ord(i)<48))):
                    if((i != ',')):
                        flag2 = True
                        print("Entrada inválida, por favor confira os valores e digite novamente")
                        i = lista[len(lista)-1]
            if flag2 == False:
                flag = False
   
    lista = lista.split(',')
    for i in lista:
        if(i != ','):
            poli.append(int(i)) 
            print(poli)
    return  poli

def gerarfuncao(poli):
    return lambda x : polinomio(x,poli)
