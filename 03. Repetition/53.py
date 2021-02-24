# Detector de Palíndromo, OBS: jeito simplificao
frase = str(input("Digite uma frase: ")).upper().replace(" ", "")
if frase == frase[::-1]:
    print(f"A frase {frase} e PALINDRONA, e sua inversa e {frase[::-1]}")
else:
    print(f"A frase {frase} e NAO E PALINDRONA, e sua inversa e {frase[::-1]}")