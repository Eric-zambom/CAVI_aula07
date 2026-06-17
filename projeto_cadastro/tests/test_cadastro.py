import pytest
from src.cadastro import cadastrar_usuario

@pytest.fixture
def banco_de_dados_mock():
    # Simulando um banco de dados simples (dict)
    return {"existente@email.com": {"id": 1, "senha": "hash"}}

def test_cadastro_com_sucesso(banco_de_dados_mock):
    resultado = cadastrar_usuario(banco_de_dados_mock, "novo@email.com", "SenhaForte123")
    
    assert resultado["sucesso"] is True
    assert "id" in resultado
    assert "novo@email.com" in banco_de_dados_mock

def test_falha_senha_curta(banco_de_dados_mock):
    resultado = cadastrar_usuario(banco_de_dados_mock, "teste@email.com", "curta12")
    
    assert resultado["sucesso"] is False
    assert resultado["erro"] == "Senha deve ter pelo menos 8 caracteres"
    assert "teste@email.com" not in banco_de_dados_mock

def test_falha_email_existente(banco_de_dados_mock):
    resultado = cadastrar_usuario(banco_de_dados_mock, "existente@email.com", "OutraSenha123")
    
    assert resultado["sucesso"] is False
    assert resultado["erro"] == "Email já registrado"