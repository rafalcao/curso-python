#coding: utf-8
"""
Curso Python - Udemy
Autor: Rafael Falcão

Manipulação de Dados
"""

num_int = 5
num_dec = 7.3
val_str = "qualquer texto"

print("O decimal é : ", num_dec)
print("O inteiro é : %i" %num_int)
print("A string é : " + val_str)



print("Concatenando decimal: ", num_dec)
print("Concatenando decimal: %.5f" %num_dec)  #5 casas decimais
print("Concatenando decimal: " + str(num_dec))  #convertendo decimal em string

print("Concatenando string: %s" %val_str)