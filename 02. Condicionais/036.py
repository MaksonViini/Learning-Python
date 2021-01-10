# Aprovando Empréstimo
print("*" * 22)
print("Analisando emprestimo".upper())
print("*" * 22)
valor = float(input("Valor da casa: R$ "))
salario = float(input("Seu salario: R$ "))
anos = int(input("Quantas parcelas: "))
print(f"Para pagar uma casa de R$ {valor:.2f} em {anos} anos ")
print(f"E a prestacao sera de {valor / (anos * 12):.2f}")
if (valor / (anos * 12)) > (salario * 0.3):
    print("Emprestimo negado")
else:
    print("Emprestimo aprovado")
