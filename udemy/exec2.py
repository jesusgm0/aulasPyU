# frase = " O Python é uma linguagem de programação"\
#     "multiparadigma."\
#     "Criado por Guido Van Rossum."
    
# i = 0

# qtd_atual = 0
# letra_que_apareceu_mais_vezes = ""

# while i < len(frase):
#     letra_atual = frase[i]
#     qtd_vezes_letra_apareceu_atual = frase.count(letra_atual) 
    
#     if letra_atual == " ":
#         i+=1
#         continue
    
#     if qtd_atual < qtd_vezes_letra_apareceu_atual:
#         qtd_atual = qtd_vezes_letra_apareceu_atual
#         letra_que_apareceu_mais_vezes = letra_atual
    
#     i+=1
    
# print(
#     'A letra que apareceu mais vezes foi '
#     f'"{letra_que_apareceu_mais_vezes}", que apareceu '
#     f'{qtd_atual} x'
#     )

# senha_salva = "123456"
# senha_digitada = ""
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')
    
#     repeticoes += 1
    
#     print(f' Quantidade de erros:{repeticoes}')
    
# print(f'acertou na {repeticoes} tentativa')

# No caso anterior, o while é mais útil, pois
# Não sabemos quantas vezes o loop será necessário
    
# texto = "O filósofo Python"
# novo_texto = ""

# for letra in texto:
#     novo_texto += f"*{letra}"
#     print(letra)
    
# print(novo_texto)

# numeros = range(5, 10, 1)

# for numero in numeros:
#     print(numero)

