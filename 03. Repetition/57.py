sexo = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
while sexo != 'M' or sexo != 'F':
    if sexo in "MmFf":
        print(f"O sexo {sexo} foi registrado")
        break
    else:
        sexo = str(input("Sexo invalido, por favor Informe seu sexo [M/F]: ")).strip().upper()[0]
