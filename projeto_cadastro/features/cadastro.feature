# language: pt

Funcionalidade: Cadastro de Usuário
  Para acessar a plataforma
  Como um visitante
  Eu quero me cadastrar usando email e senha

  Cenário: Cadastro realizado com sucesso
    Dado que o email "novo@email.com" não está registrado
    E a senha é "SenhaForte123"
    Quando eu tento realizar o cadastro
    Então a conta deve ser criada com sucesso
    E o sistema deve retornar um ID de usuário válido

  Cenário: Falha por senha muito curta
    Dado que o email "teste@email.com" não está registrado
    E a senha é "curta12"
    Quando eu tento realizar o cadastro
    Então o sistema deve rejeitar o cadastro
    E retornar um erro de validação de senha

  Cenário: Falha por email já existente
    Dado que o email "existente@email.com" já está registrado
    E a senha é "SenhaForte123"
    Quando eu tento realizar o cadastro
    Então o sistema deve rejeitar o cadastro
    E retornar um erro de conta duplicada