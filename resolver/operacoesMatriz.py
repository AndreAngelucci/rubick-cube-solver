def linhaParaLinha(matrizOrigem, matrizDestino, linhaOrigem, linhaDestino, inverter):
    linha = matrizOrigem[linhaOrigem][::-1] if inverter else matrizOrigem[linhaOrigem]
    matrizDestino[linhaDestino] = linha
    return matrizDestino

def colunaParaColuna(matrizOrigem, matrizDestino, colunaOrigem, colunaDestino, inverter):
    arrayColOrigem = [i[colunaOrigem] for i in matrizOrigem]
    if (inverter):        
        arrayColOrigem = arrayColOrigem[::-1]
    for i in range(0, len(matrizDestino)):
        matrizDestino[i][colunaDestino] = arrayColOrigem[i]
    return matrizDestino

def linhaParaColuna(matrizOrigem, matrizDestino, linhaOrigem, colunaDestino, inverter):
    linha = matrizOrigem[linhaOrigem][::-1] if inverter else matrizOrigem[linhaOrigem]
    for i in range(0, len(matrizDestino)):
        matrizDestino[i][colunaDestino] = linha[i]
    return matrizDestino

def colunaParaLinha(matrizOrigem, matrizDestino, colunaOrigem, linhaDestino, inverter):
    arrayColOrigem = [i[colunaOrigem] for i in matrizOrigem]
    if (inverter):        
        arrayColOrigem = arrayColOrigem[::-1]
    matrizDestino[linhaDestino] = arrayColOrigem
    return matrizDestino