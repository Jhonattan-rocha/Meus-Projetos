from Curos_Python_curemvid.Uteis.Cursoemvídeo import Exer111M


def resumoprecos(preco, Pord, PorA):
    print("-" * 30)
    print(f"{'Lista de preços':-^30}")
    print("-" * 30)
    print(f"Preço: {'R$':>13}{preco}")
    print(f"Dobro: {Exer111M.dobro(preco, True):>20}")
    print(f"Metade: {Exer111M.metade(preco, True):>18}")
    print(f"{PorA}% de aumento: {Exer111M.aumentar(preco, PorA, True)}")
    print(f"{Pord}% de desconto: {Exer111M.diminuir(preco, Pord, True)}")
