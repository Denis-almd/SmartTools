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

### 📊 Leitores de Dados (Readers)

O SmartTools inclui um sistema robusto de leitura de dados com as seguintes páginas:

#### BDV Consolidado Reader
Ferramenta para leitura e análise de relatórios BDV Consolidado:
- Leitura de arquivos Excel
- Processamento automático de dados
- Validação de formato
- Exibição de resultados processados

#### Utilização Reader
Ferramenta para leitura e análise de dados de utilização:
- Importação de arquivos Excel
- Análise de métricas de utilização
- Interface intuitiva para visualização

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
streamlit run app.py #app.py é o "main" do projeto e esse comando do streamlit, passa justamente ele para iniciar.
```

A aplicação será aberta automaticamente no seu navegador em `http://localhost:8501`

## 📁 Estrutura do Projeto

```
SmartTools/
├── app.py                      # Ponto de entrada da aplicação
├── README.md                   # Documentação do projeto
├── requirements.txt            # Dependências Python
├── .gitignore                  # Arquivos ignorados pelo Git
├── logs/                       # Diretório de logs da aplicação
│
├── project/
│   ├── UI/                     # Interface do usuário
│   │   ├── side_bar.py         # Barra lateral de navegação
│   │   └── pages/              # Páginas da aplicação
│   │       ├── base_page.py    # Classe base para páginas
│   │       ├── page_base_reader.py  # Classe base para páginas de leitura
│   │       ├── page_manager.py # Gerenciador de páginas
│   │       ├── home/           # Página inicial
│   │       ├── about/          # Página sobre
│   │       ├── BDV_consolidado_reader/  # Leitor BDV Consolidado
│   │       └── utilizacao_reader/       # Leitor de utilização
│   │
│   ├── tools/                  # Ferramentas disponíveis
│   │   ├── base_tool.py        # Classe base para ferramentas
│   │   ├── tool_manager.py     # Gerenciador de ferramentas
│   │   ├── time_converter/     # Conversor de tempo
│   │   └── json_formatter/     # Formatador JSON (em desenvolvimento)
│   │
│   ├── readers/                # Sistema de leitura de dados
│   │   ├── base_reader.py      # Classe base para leitores
│   │   └── excel_reader.py     # Leitor de arquivos Excel
│   │
│   └── utils/                  # Utilitários
│       ├── app_logs.py         # Sistema de logging
│       ├── emojis.py           # Constantes de emojis
│       └── pandas/             # Utilitários Pandas
│
└── project_data/               # Documentação técnica
    ├── CACHE_GUIDE.md
    ├── DEPENDENCIES_GUIDE.md
    ├── EXCEPTION_HANDLING_IMPROVEMENTS.md
    ├── LOGGING_GUIDE.md
    └── READER_ARCHITECTURE_GUIDE.md
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

## 📄 Como Adicionar Novos Leitores

1. **Crie a classe do leitor** herdando de `BaseReader`:

```python
from project.readers.base_reader import BaseReader

class MeuLeitor(BaseReader):
    def read(self):
        # Implemente a lógica de leitura
        pass
    
    def validate(self) -> bool:
        # Implemente a validação dos dados
        pass
```

2. **Crie a página UI** herdando de `PageBaseReader`:

```python
from project.UI.pages.page_base_reader import PageBaseReader

class MeuLeitorUI(PageBaseReader):
    def __init__(self):
        super().__init__(
            page_name="Meu Leitor",
            icon="📊",
            description="Descrição do leitor"
        )
    
    def _process_file(self, uploaded_file):
        # Implemente o processamento
        pass
    
    def process_data(self):
        # Implemente a análise dos dados
        pass
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
- **Streamlit 1.52.2**: Framework para criação de aplicações web interativas
- **Pandas 2.3.3**: Manipulação e análise de dados
- **OpenPyXL 3.1.5**: Leitura e escrita de arquivos Excel (.xlsx)
- **ABC (Abstract Base Classes)**: Padrão de design para classes base

## 🏗️ Arquitetura

O projeto utiliza os seguintes padrões de design:

- **Abstract Base Class (ABC)**: Para definir interfaces de ferramentas, páginas e leitores
- **Registry Pattern**: Para gerenciamento dinâmico de ferramentas e páginas
- **Separation of Concerns**: UI separada da lógica de negócio
- **Modular Architecture**: Fácil extensão e manutenção
- **Template Method Pattern**: Classes base definem o fluxo, subclasses implementam detalhes
- **Safe Read Pattern**: Sistema robusto de leitura com tratamento de exceções

### Sistema de Leitura de Dados

O SmartTools possui uma arquitetura robusta para leitura de dados:

- **BaseReader**: Classe abstrata que define a interface para todos os leitores
- **ExcelReader**: Implementação para leitura de arquivos Excel com suporte a múltiplas sheets
- **PageBaseReader**: Classe base para páginas que utilizam leitores de dados
- **Safe Read**: Método seguro com tratamento de exceções e logging

### Sistema de Logging (Já existe a classe, mas não implantado nas páginas)

- Logs automáticos de operações de leitura de dados
- Arquivos de log organizados por data em `logs/`
- Níveis configuráveis (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Consulte [LOGGING_GUIDE.md](project_data/LOGGING_GUIDE.md) para mais detalhes

## 📝 Licença

N/A

## 👤 Autor

Denis Almeida

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

### Diretrizes de Contribuição

1. Mantenha a arquitetura modular do projeto
2. Siga os padrões de design existentes (ABC, Registry Pattern)
3. Adicione documentação adequada para novas funcionalidades
4. Utilize o sistema de logging para operações importantes
5. Implemente tratamento de exceções robusto
6. Teste suas alterações antes de submeter

## 📧 Contato

denis.almeida@meta.com.br

---

**Desenvolvido com ❤️ por Denis Almeida**