#Questão4

#Faça uma função que receba parâmetros variáveis. Faça algumas chamadas dessa função passando valores inteiros e, de acordo com a quantidade de parâmetros recebidos, calcule a média.

def sum_average(*values):
    sum = 0
    for num in values:
        sum += num
    average = sum/len(values)
    return (f"The sum is: {sum} and the average is: {average}")

print(sum_average(3, 5, 10))
print(sum_average(7, 8, 6))
print(sum_average(2, 10, 1))
