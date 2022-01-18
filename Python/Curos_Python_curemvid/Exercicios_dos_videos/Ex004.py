algo = input("\033[1;31mDigite algo\033[m: ")

print("="*2000)
print("O tipo primitivo é: {} ".format(type(algo)))
print("O que você digitou é:\n Contem somente números? {} \n Contem somente letras? {} \n Contem letras ou números? {}"
      " \n Contem apenas um espaço? {} ".format(algo.isnumeric(), algo.isalpha(), algo.isalnum(), algo.isspace()))
print("Está somente em maiúsculas ? {} ".format(algo.isupper()))
print(f"Está em minúsculas ? {algo.islower()} ")
print("="*2000)