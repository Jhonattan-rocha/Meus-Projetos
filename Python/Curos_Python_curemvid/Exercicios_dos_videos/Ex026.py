nome = input("Digite uma frase: ").lower()
aq = nome.count("a")
au = nome.split()
print("Na frase tem {} lestras as \nA letra a aparece primeiramente na posição {}\n "
      "por ultimo, na ultima palavra, na posição {}".format(aq, nome.find("a")+1, au[len(au)-1].find("a")))
