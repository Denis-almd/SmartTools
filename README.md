# 🛠️ SmartTools

Uma coleção de ferramentas úteis desenvolvidas em Python com Streamlit para aumentar sua produtividade no dia a dia.

## 📋 Sobre o Projeto

SmartTools é uma aplicação web modular que fornece diversas ferramentas práticas em uma interface intuitiva. O projeto foi desenvolvido com arquitetura extensível, permitindo fácil adição de novas ferramentas.

## ✨ Ferramentas Disponíveis

### ⏰ Time Converter
Converte tempo entre formato HH:MM:SS e segundos totais:
- **HH:MM:SS → Segundos**: Converte horários para segundos
- **Segundos → HH:MM:SS**: Converte segundos para formato de tempo
- Validação automática de entradas
- Interface intuitiva com colunas lado a lado

### 📊 Utilizacao Reader
Ferramenta para leitura e análise de dados de utilização.

## 🚀 Como Usar

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd SmartTools
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv .venv
```

3. Ative o ambiente virtual:
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executar a Aplicação

```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no seu navegador em `http://localhost:8501`

## 📁 Estrutura do Projeto

```
SmartTools/
├── app.py                      # Ponto de entrada da aplicação
├── README.md                   # Documentação do projeto
├── requirements.txt            # Dependências Python
├── .gitignore                  # Arquivos ignorados pelo Git
│
└── project/
    ├── UI/                     # Interface do usuário
    │   ├── side_bar.py         # Barra lateral de navegação
    │   └── pages/              # Páginas da aplicação
    │       ├── base_page.py    # Classe base para páginas
    │       ├── page_manager.py # Gerenciador de páginas
    │       ├── home/           # Página inicial
    │       ├── about/          # Página sobre
    │       └── utilizacao_reader/
    │
    ├── tools/                  # Ferramentas disponíveis
    │   ├── base_tool.py        # Classe base para ferramentas
    │   ├── tool_manager.py     # Gerenciador de ferramentas
    │   ├── time_converter/     # Conversor de tempo
    │   └── json_formatter/     # Formatador JSON
    │
    └── utils/                  # Utilitários
        ├── emojis.py           # Constantes de emojis
        └── pandas/             # Utilitários Pandas
```

## 🔧 Como Adicionar Novas Ferramentas

1. **Crie uma nova pasta** em `project/tools/` com o nome da ferramenta

2. **Implemente a classe da ferramenta** herdando de `BaseTool`:

```python
from project.tools.base_tool import BaseTool
import streamlit as st

class MinhaFerramenta(BaseTool):
    def get_name(self) -> str:
        return "Minha Ferramenta"
    
    def get_icon(self) -> str:
        return "🎯"
    
    def get_description(self) -> str:
        return "Descrição da minha ferramenta"
    
    def render(self):
        st.header("Título da Ferramenta")
        # Implemente a UI da ferramenta aqui
```

3. **Registre a ferramenta** em `project/tools/tool_manager.py`:

```python
from project.tools.minha_ferramenta.minha_ferramenta_ui import MinhaFerramenta

class ToolRegister:
    _tools: list[type[BaseTool]] = [
        TimeConverter,
        MinhaFerramenta,  # Adicione aqui
    ]
```

## 🔧 Como Adicionar Novas Páginas

1. **Crie uma nova pasta** em `project/UI/pages/` com o nome da página

2. **Implemente a classe da página** herdando de `BasePage`:

```python
from project.UI.pages.base_page import BasePage
import streamlit as st

class MinhaPagina(BasePage):
    def get_name(self) -> str:
        return "Minha Página"
    
    def render(self):
        st.title("Título da Página")
        # Implemente o conteúdo da página aqui
```

3. **Registre a página** em `project/UI/pages/page_manager.py`:

```python
from project.UI.pages.minha_pagina.minha_pagina_ui import MinhaPagina

class PageManager:
    _pages: list[type[BasePage]] = [
        HomePage,
        MinhaPagina,  # Adicione aqui
        AboutPage
    ]
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**: Linguagem de programação
- **Streamlit**: Framework para criação de aplicações web
- **Pandas**: Manipulação e análise de dados (se aplicável)
- **ABC (Abstract Base Classes)**: Padrão de design para classes base

## 🏗️ Arquitetura

O projeto utiliza os seguintes padrões de design:

- **Abstract Base Class (ABC)**: Para definir interfaces de ferramentas e páginas
- **Registry Pattern**: Para gerenciamento dinâmico de ferramentas e páginas
- **Separation of Concerns**: UI separada da lógica de negócio
- **Modular Architecture**: Fácil extensão e manutenção

## 📝 Licença

N/A

## 👤 Autor

Denis Almeida

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## 📧 Contato

denis.almeida@meta.com.br