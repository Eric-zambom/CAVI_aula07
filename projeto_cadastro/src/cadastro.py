import uuid

def cadastrar_usuario(db: dict, email: str, senha: str) -> dict:
    """
    Função de produção para cadastro de usuário.
    """
    if len(senha) < 8:
        return {"sucesso": False, "erro": "Senha deve ter pelo menos 8 caracteres"}
        
    if email in db:
        return {"sucesso": False, "erro": "Email já registrado"}
        
    # Simulando a criação no banco
    novo_id = str(uuid.uuid4())
    db[email] = {"id": novo_id, "senha": senha} # Em produção, use hash para a senha!
    
    return {"sucesso": True, "id": novo_id}