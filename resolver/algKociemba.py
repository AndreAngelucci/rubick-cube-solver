from kociemba import solve
from rubik import *
from enums import Faces

def createDefinitionString(cube):
    #string de definicao do cubo que o algotimo entende
    #padrao: UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB
    #identifica a cor dos centros de face:
    colorU = cube.faceSuperior[1][1]
    colorR = cube.faceDireita[1][1]
    colorF = cube.faceFrente[1][1]
    colorD = cube.faceInferior[1][1]
    colorL = cube.faceEsquerda[1][1]
    colorB = cube.faceCostas[1][1]
    auxDefString = ""
    #identifica as cores nas matrizes do cubo. 
    for f in (
        Faces.superior,
        Faces.direita,
        Faces.frente,
        Faces.inferior,
        Faces.esquerda,
        Faces.costas
    ):
        for l in range(0, 3):
            for c in range(0, 3):
                colorAux = cube.retornaFace(f)[l][c]
                if (colorAux == colorU):
                    auxDefString += "U"
                elif (colorAux == colorR):
                    auxDefString += "R"
                elif (colorAux == colorF):
                    auxDefString += "F"
                elif (colorAux == colorD):
                    auxDefString += "D"
                elif (colorAux == colorL):
                    auxDefString += "L"
                elif (colorAux == colorB):
                    auxDefString += "B"
    return auxDefString

def translateSolution(solutionString):
    #traduz uma string de solucao para os movimentos padroes da 
    #classe rubik
    movs = []
    for mov in solutionString.split(' '):
        movs.append(stringToMov(mov))
    return movs

def resolver(cube):
    #resolve o cubo e devolve uma lista de movimentos
    definitionString = createDefinitionString(cube)
    print 'String de definicao: '+ definitionString
    solutionString = solve(definitionString)
    print 'Solucao            : '+ solutionString
    movArray = translateSolution(solutionString)
    for mov in movArray:
        cube.mover(mov)
        