# Funções para votação
def voto (ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        print("Voto NEGADO!")
    elif idade >= 16 and idade < 18:
        print("Voto OPCIONAL!")
    else:
        print("Voto OBRIGATORIO!")
voto(int(input("Em que ano voce nasceu? ")))