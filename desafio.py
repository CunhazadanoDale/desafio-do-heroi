# Entrada de dados
nome = input("Digite o nome do herói: ")
xp = int(input("Digite a quantidade de XP do herói: "))

# Dicionário com as faixas de XP e seus respectivos níveis
lista_xp = {
    "Ferro": (0, 1000),
    "Bronze": (1001, 2000),
    "Prata": (2001, 5000),
    "Ouro": (5001, 7000),
    "Platina": (7001, 8000),
    "Ascendente": (8001, 9000),
    "Imortal": (9001, 10000),
    "Radiante": (10001, float('inf'))
}

# Verifica o nível com base nas faixas de XP
nivel = next(nivel for nivel, (min_xp, max_xp) in lista_xp.items() if min_xp <= xp <= max_xp)

# Saída formatada
print(f"O Herói {nome} está no nível {nivel}")
