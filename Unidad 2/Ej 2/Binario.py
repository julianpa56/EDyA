
def convertirABinario(numero):
    
    binarioInverso=[]

    while numero != 0:
        modulo= numero % 2
        cociente= numero // 2
        binarioInverso.append(modulo)
        numero= cociente
    binario=[]
    for i in reversed(binarioInverso):
        binario.append(i)
    

    return "".join(map(str, binario))