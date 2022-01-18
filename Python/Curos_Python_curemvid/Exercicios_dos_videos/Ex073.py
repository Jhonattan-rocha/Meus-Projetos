times = ('Palmeiras', 'Cruzeiro', 'Grêmio', 'Santos', 'Corinthians', 'Flamengo', 'Atlético mineiro',
         'Athletico Paranaense',
         'Internacional', 'Chapecoense', 'Botafogo', 'São Paulo', 'Fluminense', 'Vasco da Gama', 'Bahia', 'Sport',
         'Vitória', 'Ponte Preta', 'América', 'Coritiba')

for c in range(0, 5):
    print("O ", (c+1), f"° colocado foi: {times[c]}")
print("\n")
for c in range(15, 20):
    print("O ", (c+1), f"° colocado foi: {times[c]}")
print("\n")
print(f"A Chapecoense ficou na posição: {int(times.index('Chapecoense')+1)}")
times = sorted(times)
print("\n")
print("A lista em ordem alfabética é: ")
for c in range(0, 20):
    print((c+1), f"° time: {times[c]}")
print("\n")
