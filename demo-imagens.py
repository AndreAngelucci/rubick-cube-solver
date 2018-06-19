from vision.analiseCores import gerarRubikImagem
from util.funcoesUteis import printLogo
from rubik.rubik import *
from rubik.algKociemba import resolver
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#gera uma classe tipo Rubik de acordo com as imagens
#e as configuracoes de coordenadas informada

pathim1 = './fotos/f1.png'
pathim2 = './fotos/f2.png'
pathcoordenadas = './coordenadas.conf'

printLogo()
print('Demonstracao do reconhecimento de cor das pecas do cubo.')
raw_input('\nPressione Enter para continuar...')

cubo = gerarRubikImagem(
    pathim1, pathim2, pathcoordenadas    
)

print('Estrutura gerada atraves do reconhecimento de cores:\n\n')
cubo.representacaoGrafica()

img1 = mpimg.imread(pathim1)
img2 = mpimg.imread(pathim2)
fig = plt.figure(1)
ax1 = fig.add_subplot(121)
ax1.imshow(img1)
ax2 = fig.add_subplot(122)
ax2.imshow(img2)
plt.show()

raw_input('Pressione Enter para encontrar a solucao...')
resolver(cubo)
print('\n\n')
cubo.representacaoGrafica()