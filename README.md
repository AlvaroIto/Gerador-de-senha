# 🧩 Gerador de Senhas — CLI (Nível 1)

## Descrição
Aplicação de linha de comando (CLI) que gera senhas seguras com opções personalizáveis, como:
- comprimento configurável;
- inclusão de letras maiúsculas, minúsculas, números e símbolos;
- opção de salvar as senhas geradas em arquivo.

Este projeto foi desenvolvido **com auxílio do ChatGPT (OpenAI)** como parte do aprendizado de fundamentos, boas práticas e organização de projetos em Python.

---

## 🎯 Objetivo
Praticar:
- lógica de programação e modularização;
- uso de `random` e `string`;
- boas práticas PEP8;
- funções bem organizadas e reutilizáveis;
- entrada e saída via terminal (CLI).

---

## 🧱 Estrutura do Projeto
gerador-de-senha/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│ ├── init.py
│ ├── main.py
│ ├── generator.py
│ └── storage.py
└── tests/
└── test_generator.py

---

## ⚙️ Instalação
1. Clone o repositório ou copie os arquivos do projeto.  
2. Crie e ative um ambiente virtual:
   python -m venv .venv
   source .venv/bin/activate   # mac/linux
   .venv\Scripts\activate      # windows
3. Instale as dependências:
    pip install -r requirements.txt

🚀 Uso

Gerar uma senha simples:
    - python src/main.py --length 16

Gerar uma senha com números e símbolos:
    - python src/main.py --length 20 --no-lower

Salvar a senha em arquivo:
    - python src/main.py --length 20 --save passwords.txt

🧪 Testes

Para executar os testes:
    - pytest

Exemplo de testes básicos está em tests/test_generator.py.

🧑‍💻 Créditos

Projeto desenvolvido por Alvaro Ito com o auxílio do ChatGPT (OpenAI), como parte do aprendizado prático de Python e boas práticas de desenvolvimento de software.