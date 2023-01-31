#Questão1

#Criar uma função chamada "imprime_tabuada" e, usando o for, imprimir as tabuadas de a 1 a 10.

def imprime_tabuada():
    for a in range(1, 11):
        for b in range(1, 11):
            resultado = a * b
            print(f"{a} x {b} = {resultado}")

imprime_tabuada()
