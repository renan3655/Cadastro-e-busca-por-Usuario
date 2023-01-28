clientes = []  # lista para armazenar registros de clientes

def registrar_cliente(nome, email, telefone):
  # cria um novo registro de cliente
  novo_cliente = {
    'nome': nome,
    'email': email,
    'telefone': telefone
  }
  # adiciona o novo cliente à lista de clientes
  clientes.append(novo_cliente)

def buscar_cliente(telefone):
  # pesquisa por um cliente com o telefone dado
  for cliente in clientes:
    if cliente['telefone'] == telefone:
      return cliente
  # se nenhum cliente for encontrado, retorna None
  return None

def exibir_menu():
  print('1. Cadastrar cliente')
  print('2. Buscar cliente')
  print('3. Sair')
  opcao = int(input('Escolha uma opção: '))
  return opcao

while True:
  opcao = exibir_menu()
  if opcao == 1:
    # obtém a entrada do usuário
    nome = input('Digite o nome: ')
    email = input('Digite o email: ')
    telefone = input('Digite o telefone: ')
    # registra o cliente
    registrar_cliente(nome, email, telefone)
  elif opcao == 2:
    telefone = input('Digite o telefone do cliente: ')
    cliente = buscar_cliente(telefone)
    if cliente:
      print(f'Nome: {cliente["nome"]}')
      print(f'Email: {cliente["email"]}')
      print(f'Telefone: {cliente["telefone"]}')
    else:
      print('Cliente não encontrado')
  elif opcao == 3:
    break

print(clientes)  # imprime a lista de clientes
