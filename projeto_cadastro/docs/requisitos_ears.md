# Requisitos do Módulo de Cadastro (Padrão EARS)

1. **[Ubiquitous]** O sistema deve exigir um endereço de email e uma senha para o cadastro.
2. **[State-driven]** Enquanto a senha tiver menos de 8 caracteres, o sistema deve rejeitar a tentativa de cadastro com um erro de validação.
3. **[State-driven]** Enquanto o email fornecido já estiver registrado no banco de dados, o sistema deve rejeitar o cadastro com um erro de duplicidade.
4. **[Event-driven]** Quando o usuário submeter dados válidos (email não registrado e senha com 8 ou mais caracteres), o sistema deve criar a nova conta.
5. **[Event-driven]** Quando a conta for criada com sucesso, o sistema deve retornar o ID do novo usuário.