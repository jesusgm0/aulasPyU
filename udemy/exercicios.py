# # contador = 0
# # while contador < 50:
# #     contador += 1

# #     if contador == 6:
# #       print("Não mostrar o número 6")
# #       continue

# #     # if contador >= 10 and contador <= 20:
# #       continue
# #     print(contador)
# #     if contador == 23:
# #         break

# # print('Fim do programa')


# qtd_linhas = 10
# qtd_colunas = 10
# linha = 1

# while linha <= qtd_linhas:
#     coluna = 1
#     while coluna <= qtd_colunas:
#         print("Linha:", linha, "Coluna:", coluna)
#         coluna += 1
#     linha += 1


# Calculadura com while
while True:
    numero_1 = input("Digite o primeiro número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador(=, -, *, /): ")
    
    numeros_validos = None
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
        if numeros_validos is None:
            print("Um ou ambos dos números digitados são inválidos.")
            continue
    
    operadores_permitidos = '+-*/'
    if operador not in operadores_permitidos:
        print("Operador inválido.")
        continue
    
    if len(operador) > 1:
        print("Digite apenas um operador")
        continue
    
    print("Realizando a operação, o resultado estará abaixo:")
    if operador == "+":
        print(f'{numero_1_float} + {numero_2_float} = ', numero_1_float + numero_2_float)
    elif operador == "-":
        print(f'{numero_1_float} - {numero_2_float} = ', numero_1_float - numero_2_float)
    elif operador == "*":
        print(f'{numero_1_float} * {numero_2_float} = ', numero_1_float * numero_2_float)
    elif operador == "/":
        print(f'{numero_1_float} / {numero_2_float} = ', numero_1_float / numero_2_float)
    else:
        ("Algo de errado aconteceu.")
    

    sair = input("Quer sair? [s]im: ").lower().startswith("s")

    if sair:
        break