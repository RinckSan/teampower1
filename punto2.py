#Declarando la funcion 
def clasificarNumero(numero):
    return(numero > 10)

#Funcion lambda
funcionlambda=lambda numero: numero>10



#ESTO NO ES FUNCION ES CODIGO SECUENCIAL NORMAL
lista = [1,5,12,25,8]
for numero in lista:
    print(funcionlambda(numero))
