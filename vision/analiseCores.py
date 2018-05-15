from util.enums import *
from rubik.rubik import *
import ConfigParser
import cv2

def detectaCor(bgr):
	# analisa um vetor bgr (blue, gren, red)
	# e retorna sua cor correspondente.
	percAzul = (bgr[0] * 100) / 255
	percVerde = (bgr[1] * 100) / 255
	percVermelho = (bgr[2] * 100) / 255
	if ((percAzul >= 40) and (percVerde >= 40) and (percVermelho >= 40)):
		return Cores.branco
	if ((percVermelho > 60) and (percVermelho > (percAzul + percVerde))):
		return Cores.laranja
	if ((percVermelho > percAzul) and (percVermelho > percVerde)):
		return Cores.vermelho
	if ((percVerde > percVermelho) and (percVermelho > percAzul)):
		return Cores.amarelo
	if ((percVerde > percAzul) and (percAzul > percVermelho)):
		return Cores.verde
	if ((percAzul > percVerde) and (percVerde > percVermelho)):
		return Cores.azul	
	return Cores.indefinida

def analisaArea(imagem, centro, alcance):
	if (imagem is None):
		raise Exception("Imagem invalida")
	#imagem que sera analisada
	#centro: pixel que sera considerado como centro de um quadrado de analise
	#alcance: distancia entre o centro e os lados desse quadrado.
	iniX = int(centro[0]) - alcance
	fimX = int(centro[0]) + alcance
	iniY = int(centro[1]) - alcance
	fimY = int(centro[1]) + alcance
	#captura a cor dos pixels da area
	resultados = []
	for x in range(iniX, fimX + 1):	
		for y in range(iniY, fimY + 1):
			resultados.append(imagem[x, y])
	#calcula um rgb medio com os array
	#descartando pixels com valores fora da media (lixo)
	rgbMedia = [0, 0, 0]
	for item in resultados:
		rgbMedia[0] += item[0] #R
		rgbMedia[1] += item[1] #G
		rgbMedia[2] += item[2] #B
	#calcula a media
	rgbMedia = [
		rgbMedia[0] / len(resultados),
		rgbMedia[1] / len(resultados),
		rgbMedia[2] / len(resultados),
	]	
	#retorna a cor da media encontrada
	return detectaCor(rgbMedia)

def strToFace(str):
	#converte uma string para uma face (enums.Faces)	
	return [
		Faces.esquerda, Faces.superior, Faces.frente, Faces.inferior,
		Faces.direita, Faces.costas
	][
		['face_esquerda', 'face_superior', 'face_frente', 'face_inferior',
		'face_direita', 'face_costas'].index(str)
	]

def gerarRubikImagem(pathImagem, pathCoordenadas):
	#recebe o path de uma imagem e gerar um objeto Rubik
	#atraves da analise das cores nas coordenadas determinadas
	#no arquivo coordenadas.conf	
	imCubo = cv2.imread(pathImagem)
	config = ConfigParser.ConfigParser()
	config.read(pathCoordenadas)
	#cubo vazio
	cubo = Rubik()
	for conf in [
		'face_esquerda', 'face_superior', 'face_frente',
		'face_inferior', 'face_direita', 'face_costas'
	]:
		#alimenta a face corrente
		faceCorrente = cubo.retornaFace(strToFace(conf))
		#captura as coordenadas em todas as faces
		for (key, value) in (config.items(conf)):
			cx = int(key[0])
			cy = int(key[1])
			coords = value.split(',')
			faceCorrente[cx][cy] = analisaArea(imCubo, coords, 10)
	return cubo
