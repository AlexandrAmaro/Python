from ex109_FormatandoMoedasMelhorado import moeda

p = float(input('Digite o preço: €'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')    # → True da formatação da moeda
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
