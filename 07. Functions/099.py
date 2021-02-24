# Função que descobre o maior
def maior (*valor):
    print("-=-" * 15)
    print("Analisando os valores passados...")
    print(f"{valor} Foram informados {len(valor)} ao todo ")
    print(f"O maior valor informado foi {max(valor)} ")
    print("-=-" * 15)
maior(1, 2, 3, 5)