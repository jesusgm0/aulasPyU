for i in range(10):
    if i ==2:
        print('i é 2, pulando...')
        continue
    
    if i == 8:
        print('i é 8, laço interrompido')
        break
    
    for j in range(1, 3):
        print(i, j)
else:
    print("Laço finalizado.")