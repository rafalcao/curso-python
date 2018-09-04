#coding: utf-8
"""
Curso Python - Udemy
Autor: Rafael Falcão

Decisao
"""

acao = int(input("Digite '1' para sim e '2' para não: "))

if(acao==1):
    print("Você disse que sim!")
elif(acao==2):
    print("Você disse que não!")
else:
    print("Valor não encontrado!")


idade = int(input("Digite sua idade: "))
if(idade<=0):
    print("A sua idade não pode ser menor ou igual que 0")
elif(idade>150):
    print("A sua idade não pode ser maior que 150 anos.")
elif(idade<18):
    print("Você precisa ter mais de 18 anos.")
else:
    print("Você tem: %i anos" %idade)