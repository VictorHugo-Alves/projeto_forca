#import
import random
from os import system, name

#Função pra limpar a tela em cada execução
def limpa_tela():
	if name == 'nt':
		_= system('cls')

def game():
	limpa_tela()
	print('\n Bem-vindo(a) ao jogo da forca!')
	print('Adivinhe a palavra abaixo:\n')

	#lista de palavras para o jogo
	palavras = ['banana','abacate','uva','morango','laranja']

	#Escolha aleatoria de palavras
	palavra = random.choice(palavras)

	#list comp
	letras_descobertas = ['_' for letra in palavra]

	#chances
	chances = 6

	#lista para letras erradas
	letras_erradas = []

	#loop enquanto chances for maior q zero
	while chances > 0:
		print(' '.join(letras_descobertas))
		print('\n Chances restantes:',chances)
		print('Letras erradas:',' '.join(letras_erradas))

		#tentativa
		tentativa = input('\nDigite uma letra:').lower()
		
		#Verificando se a letra está na palavra
		if tentativa in palavra:
			index = 0
			for letra in palavra:
				if tentativa == letra:
					letras_descobertas[index] = letra
				index += 1
		else:
			chances -= 1
			letras_erradas.append(tentativa)
			
		#Verificando se todas as letras foram descobertas
		if '_' not in letras_descobertas:
			print(f'Parabéns, você adivinhou a palavra {palavra}')
			break
game()