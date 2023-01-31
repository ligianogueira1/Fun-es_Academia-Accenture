#Questão2

#Criar uma função que receba quatro notas em valor decimal, entre 0 e 10. Caso a nota seja menor que 5, retornar "Reprovada"; caso esteja entre 5 e 7, retornar "Está na média"; e, caso seja maior que 7, retornar "Aprovada". 

def approval(note1, note2, note3, note4):
    average = (note1 + note2 + note3 + note4) / 4
    if average < 5:
        return "Failed."
    elif average > 5 and average < 7:
        return "Is in the average."
    return "Approved."

print(approval(3.0, 5.0, 4.0, 5.0))
