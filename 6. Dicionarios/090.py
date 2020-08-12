# Dicionário em Python
aluno = {str(input("Nome: ")): float(input("Media: "))}
for k, v in aluno.items():
    print(f"Nome igual a {k} e media igual a {v} ")
    print("Situacao e igual a",'Reprovado' if aluno[k] < 7 else 'Aprovado')