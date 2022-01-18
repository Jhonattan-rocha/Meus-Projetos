text = "curso em vídeo python"
print(text)
# textos em python são separados por pequenos espaço, podendo ser trabalhado apenas partes especificadas pelo
# programador

print(len(text))  # retorna o tamanho
print(text[3:12])
print(text[13:])
print(text[0::2])  # retorna as letras da primeira posição até o final pulando de dois em dois
print(text[:5])  # retorna as letras do começo ao 5(c=não considera o 5, então vai só até o 4)
print(text[2:])  # retorna da posição 2 ao fim da string
print(text.find("u"))  # retorna a posção que começa o intervalo de lestra(s) que o programador específica
print(text.count("a"))  # retorna a quantidade de vezes que o a é repetido no texto digitado

text.replace("A", "b")  # traformação, muda o que eu específiquei para outra coisa
text.upper()  # coloca em maiúsculas a string da variável
divido = text.split()

print(divido[2])

