# Gerenciador de Pagamento
print("=" * 20, "LOJAS", "=" * 20)
preco = float(input("Preco das compras: R$ "))
print("formas de pagamentos".upper())
print("[1] a vista dinheiro/cheque")
print("[2] a vista no cartao ")
print("[3] 2x no cartao ")
print("[4] 3x ou mais no cartao ")
op = int(input("Qual a sua opcao: "))

if op == 1:
    print(f"Sua compra a vista foi de R$ {preco:.2f}, e no final vai custar R$ {preco * 0.9:.2f} ")
elif op == 2:
    print(f"Sua compra a vista no cartao foi de R$ {preco:.2f}, e no final vai custar R$ {preco * 0.95:.2f} ")
elif op == 3:
    parcelas = int(input("Quantas parcelas: "))
    if parcelas <= 2:
        print(f"Sua compra foi parcelada em {parcelas}x foi de R$ {preco:.2f}, e no final vai custar R$ {preco:.2f} ")
    else:
        print(f"Sua compra foi parcelada em {parcelas}x foi de R$ {preco:.2f}, e no final vai custar R$ {preco * 1.2:.2f} ")
elif op == 4:
    if parcelas <= 2:
        print(f"Quantidade de parcelas invalidas para essa opcao")
    else:
        print(f"Sua compra foi parcelada em {parcelas}x foi de R$ {preco:.2f}, e no final vai custar R$ {preco * 1.2:.2f} ")
