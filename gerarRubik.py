from vision.analiseCores import gerarRubikImagem
from rubik.rubik import *

#gera uma classe tipo Rubik de acordo com a imagem
#e as configuracoes de coordenadas informada
gerarRubikImagem('./fotos/frente.jpg', './coordenadas.conf').representacaoGrafica()
