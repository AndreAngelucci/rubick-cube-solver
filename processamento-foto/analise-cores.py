import cv2 as cv
from enums import Cores

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
	#imagem que sera analisada
	#centro: pixel que sera considerado como centro de um quadrado de analise
	#alcance: distancia entre o centro e os lados desse quadrado.
	iniX = centro[0] - alcance
	fimX = centro[0] + alcance
	iniY = centro[1] - alcance
	fimY = centro[1] + alcance
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

#corta a imagem do cubo
cubo = cv.imread('./foto-cubo.jpg')
print(analisaArea(cubo, [661, 404], 15))
