# 🏥 API de Agendamento Clínico - Starter Kit

Bem-vindo ao Starter Kit da API de Agendamento Clínico! Este projeto fornece toda a infraestrutura base de backend (banco de dados, autenticação, testes e permissões) para que você possa focar no desenvolvimento das regras de negócios e funcionalidades da clínica.

## 📦 O que este projeto já possui?

Este repositório foi configurado com as seguintes tecnologias e estruturas:

*   **FastAPI:** Framework moderno e de alta performance para a construção da API REST.
*   **Banco de Dados (SQLModel + SQLite):** Configuração pronta de ORM com modelos relacionais (`User`, `Patient`, `Appointment`). O banco de dados `clinica.db` é gerado automaticamente.
*   **Autenticação e Segurança:** 
    *   Geração e validação de tokens JWT (JSON Web Token).
    *   Criptografia de senhas utilizando Bcrypt (via Passlib).
*   **Controle de Acesso (RBAC):** Sistema de restrição de rotas baseado no papel do usuário (`admin`, `recepcionista`, `profissional`).
*   **Testes Automatizados (Pytest):** Suíte de testes configurada com injeção de um banco de dados temporário em memória (StaticPool), garantindo que os testes não sujem o banco de dados real da aplicação.

---

## ⚠️ Pré-requisitos

Para rodar este projeto sem conflito de bibliotecas, é **obrigatório** o uso do **Python 3.10** ou **3.11**. Versões muito recentes (como 3.12+ ou 3.14) podem apresentar incompatibilidades com versões específicas de dependências utilizadas neste kit didático.

---

## 🚀 Como configurar e executar o projeto

Siga o passo a passo abaixo no seu terminal, garantindo que você está dentro da pasta raiz do projeto.

### 1. Criar o Ambiente Virtual (venv)
É fundamental isolar as bibliotecas do projeto do restante do seu computador.
```bash
# No Mac/Linux:
python3.10 -m venv venv

# No Windows:
python -m venv venv
```

```bash
# No Mac/Linux:
source venv/bin/activate

# No Windows (Prompt de Comando):
venv\Scripts\activate

# No Windows (PowerShell):
.\venv\Scripts\Activate.ps1
```

```bash
pip install -r requirements.txt
```

```bash
python -m pytest -v
```

```bash
python main.py
```

Acessar a Documentação Interativa
Com o servidor rodando, abra o seu navegador e acesse a interface do Swagger UI:
👉 http://127.0.0.1:8000/docs

Através dessa página, você poderá criar novos usuários, fazer o login para obter o token JWT, autenticar a página (botão Authorize) e testar a criação de consultas.

