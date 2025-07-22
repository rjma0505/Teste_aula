# Programa simples de boas-vindas em Python

print("Olá turma do Python!")
print("Tudo bem!")
nome: str = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")

# Nova funcionalidade: idade
idade: int = int(input("Qual é a sua idade? "))
print(f"{nome}, você tem {idade} anos!")

if idade >= 18:
    print("Seja bem-vindo(a) ao mundo adulto!")
else:
    print("Aproveite a juventude!")

# Função de saudação
def saudacao(nome: str, idade: int):
    print(f"Olá, {nome}, você tem {idade} anos!")

saudacao(nome, idade)
