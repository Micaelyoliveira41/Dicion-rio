pessoa: {''}

# adicionando uma nova chave ao dicionário
pessoa: {'nome'} = input((f'Informe o nome do usuário:'))
pessoa['CPF'] = input((f'Informe o CPF do usuário:'))
# exibindo os dados do dicionário
print(pessoa.get('nome'))
print(pessoa.get('CPF'))
