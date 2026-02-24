nome = 'Carlos'
notas = { 'Ana': 9 , 'Bruno': 6 , 'Carlos': 7 , 'Daniela': 8}

for aluno in notas:
    if aluno == nome:
        print(notas[aluno])
        break
    
    else:
        print('Nome não encontrado.')
        
        
'''n = 10
        
soma = 0 
i = 1
        
while i <= n:
            soma = soma + i 
            i = i+1 
            
print("A soma é", soma)'''
        