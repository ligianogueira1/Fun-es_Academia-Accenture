#Questão3

#Faça uma função que receba 5 números e imprima a soma e a média destes.

def sum_average(value1, value2, value3, value4, value5):
    sum = value1 + value2 + value3 + value4 + value5
    average = sum/5
    return (f"The sum is: {sum}\n"f"The average is: {average}")

print(sum_average(3.0, 5.0, 4.0, 5.0, 6.0))
