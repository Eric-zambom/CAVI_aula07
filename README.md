# Módulo de Cadastro: Fluxo de Engenharia de Software

Este é um projeto em Python focado em demonstrar um fluxo de trabalho de engenharia de software rigoroso e à prova de falhas para um módulo de cadastro de usuários. O projeto integra levantamento de requisitos, especificação de comportamento, desenvolvimento guiado por testes e testes de mutação.

---

## 🛠️ Tecnologias e Ferramentas

* **Python 3** - Linguagem principal.
* **EARS** (*Easy Approach to Requirements Syntax*) - Padronização de requisitos.
* **Gherkin** - Especificação de cenários (BDD).
* **Pytest** - Framework de testes e TDD.
* **Mutmut** - Testes de mutação para garantir a resiliência da suíte de testes.

---

## 📂 Estrutura do Projeto

A arquitetura do repositório foi desenhada para separar claramente código de produção, testes, especificações e documentação:

```text
projeto/
├── docs/
│   └── requisitos_ears.md    # Requisitos do sistema padronizados
├── features/
│   └── cadastro.feature      # Especificações executáveis em formato BDD
├── src/
│   └── cadastro.py           # Código de produção (lógica de negócios)
├── tests/
│   └── test_cadastro.py      # Suíte de testes (TDD)
└── setup.cfg                 # Configuração do Mutmut
