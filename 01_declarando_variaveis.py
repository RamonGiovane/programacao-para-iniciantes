# Algoritmo 01: Declarando variaveis

# A variavel abaixo é do tipo str (string)
nome: str = "Ramon"

# As variaveis abaixo são do tipo int (inteiro)
idade: int = 18
idade_pra_votar: int = 70


# A variavel abaixo é do tipo float (número com vírgula)
preco_da_carne = 18.75

# As variaveis abaixo são do tipo bool (booleano)
gosto_de_chocolate: bool = True
gosto_de_jilo: bool = False

# O operador not inverte o sentido de um bool
verdadeiro: bool = not False
falso: bool = not True

print("verdadeiro", verdadeiro)

# Os operadores de comparacao, verificam se uma condição é verdadeira
posso_votar: bool = idade < idade_pra_votar

print('Minha idade é: ', idade)
print('A idade para votar é:', idade_pra_votar)
print('Posso votar? ', posso_votar)

