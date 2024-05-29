# Dicionário: usuário add dados
import os
#Crie um dicionário 
 
dados = {
    'Nome': input(f'Informe o nome do usuário:'), 
    'CPF': input(f'Informe o CPF do usuário:'), 
    'RG': input(f'Informe o RG do usuário:'),
    'data de nascimento': input(f'Informe a data de nascimento do usuário:'),
    'Gênero': input(f'Informe o gênero do usuário:'),
    'Email': input(f'Informe o email do usuário:'), 
    'Telefone': input(f'Informe o telefone do usuário:'), 
    'Tipo sanguíneo': input(f'Informe o tipo sanguíneo do usuário:'), 
    'Profissão' : input(f'Informe a profissão do usuário:'), 
    'Empresa': input(f'Informe a empresa do usuário:'),}

for chave in dados:
    print(f'{dados}: {dados.get(chave)}')