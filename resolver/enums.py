from enum import Enum

#enum com as cores do cubo
class Cores(Enum):
	branco = '\033[47m' + '\033[30m'+ 'B'+ '\033[0;0m'
	laranja = '\033[45m'+ 'L'+ '\033[0;0m'
	azul = '\033[44m'+ 'A'+ '\033[0;0m'
	verde = '\033[42m'+ 'R' + '\033[0;0m'
	amarelo = '\033[43m'+ 'M'+ '\033[0;0m'
	vermelho = '\033[41m'+ 'V'+ '\033[0;0m'
	indefinida = '?'

#possiveis faces do cubo
class Faces(Enum):
    frente = 0
    superior = 1
    direita = 2
    esquerda = 3
    inferior = 4
    costas = 5

#possiveis movimentos
class SentidoMovimento(Enum):
    horario = 0
    antiHorario = 1	

#tipos de peca
class Pecas(Enum):
    central = 0
    meio = 1
    lateral = 2