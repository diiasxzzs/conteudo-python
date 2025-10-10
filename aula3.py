# operadores matematicos
import math
# + <- soma: soma o valor da esquerda com o da direita
# + <- subtracao: subtrai o valor da esquerda pelo o da direita
# * <- multiplicacao: multiplica o valor da esquerda com o da direita
# / <- divisao: divideo valor da esquerda pelo da direita

# ** <- potencia: eleva o valor da esquerda pelo da direita
# math.sqrt(valor) <- raiz quadrada: tira a raiz quadrada do valor

# // <- inteiro da divisao: quanto faz uma divisao que resulta em
# valor float, retorna so a parte inteira. 10.56 retornaria apenas 10

# % <- resto da divisao:  retorna o valor do resto quando a divisao
# nao e exata. 5/2 teria o resto 1. ultil na indentificacao de valores par

valor_1 = int(input("digite o valor 1: "))
valor_2 = int(input("digite o valor 2: "))

print("os valores digitados sao", valor_1, "e ", valor_2)

resultado = valor_1 + valor_2
print("a soma dos dois valores e", resultado)

resultado = valor_1 - valor_2
print("a subtracao dos dois valores e",resultado)

resultado = valor_1 * valor_2
print("a multiplicacao dos valores e ",resultado)

resultado = valor_1/valor_2
print("a divisao dos dos valores e ", resultado)

resultado = valor_1//valor_2
print("o resultado inteiro da divisao dos valores e", resultado)

resultado = valor_1 % valor_2
print("o resto de divisao dos valores e", resultado )


resultado = valor_1 ** valor_2
print(" o resultado da potenciaacao dos valores e ", resultado)

resultado = math.sqrt(valor_1)
print("a raiz qudrada de,"valor_1,"e", resultado)

print("o valor de pi e ",math.pi)

