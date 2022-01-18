nome = input("Qual é o seu nome: ")
if nome == "Gustavo":
    print("que nome feio")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo" or nome == "Jhonattan":
    print("seu nome é bem popular no Brasil")
elif nome in "Ana claudia jéssica juliana":
    print("Bele nome")
else:
    print("Seu nome é normal")
print("tenha um bom dia, {}!!".format(nome))
