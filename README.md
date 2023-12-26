# FastAPI Avançado 2023 | 2 Projetos | TDD | PostgreSQL |  Docker

## Preparando ambiente de produção:
- Ubuntu no windows (WSL)[https://learn.microsoft.com/pt-br/windows/wsl/install]
- Controle de versionamento (Pyenv)[https://roasted-basil-9d8.notion.site/Pyenv-pt-0410a3d9ce594cc99a7fb7ca954aee52]
- Gerenciamento e embalagem de dependência em Python(Poetry)[https://python-poetry.org/docs/]
- (Docker)[https://github.com/codeedu/wsl2-docker-quickstart]

## Type int e Pydantic
1. Primeiro iniciamos nosso poetry com o comado `poetry init`.
2. Inicializamos o ambiente virtual: `poetry shell`.
3. Adicionamos nossas dependências: `poetry add pydantic`.

- TYPE INT: em python conseguimos "tipar" nossas variáveis utlizando o type int. Por exemplo:
    - dinâmico: `def f (name)`
    - type int: `def f (name: str)`

- Pydantic: Uma biblioteca Python para executar a validação de dados. Você declara a "forma" dos dados como classes com atributos.

## Sync vs Async

|     Sync      |    Async      |
| ------------- | ------------- |
| Sequencial    | Concorente    |


