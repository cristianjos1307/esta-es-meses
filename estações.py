nome = input("Digite o seu nome: ")
mes = int(input("Digite o mês que você quer consultar: "))
dia = int(input("Digite o dia que você quer consultar: "))

# Verão
if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia < 21):
    estacao = "Verão"
    
# Outono
elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia < 21):
    estacao = "Outono"
    
# Inverno
elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia < 23):
    estacao = "Inverno"
    
# Primavera
else:
    estacao = "Primavera"

print(f"Olá {nome}, a estação do ano para a data {dia}/{mes} é {estacao}.")