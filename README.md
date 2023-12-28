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

- Uma função assincrona semmpre irá retorna uma `coroutine` que é uma instância da tarefa que irá ser executada, para isso foi criando o EVENT LOOP. No python sempre para funções assincronas iremos precisar de um EVENT LOOP para orquestrar a execução da função. Também podemos executar a função assincrona dentro de outra função utilizando o `await` , porém ambos são obrigados a serem assincronos. Olhe o exemplo abaixo:
```
async def sum(a,b):
    return a +b

async def print_sum(a,b):
    result = await sum(a,b)
    print(f'resultado é igual a {result}')

event_loop = asyncio.new_event_loop()
event_loop.run_until_complete(print_sum(2,3))

```
- Exemplos de aplicação no arquivo `async_sync.py`

## Routers
- No input de dados podemos trabalhar de três formas: 
1. path parameter.
```
@router.get('/converter/{from_currency}')
def converter(from_currency: str):
    return "rota converter"
```
2. query parameter.
```
#/url?to_currencies=USD,EUR,GBP&price=5.55 
@router.get('/converter/{from_currency}')
def converter(from_currency: str,to_currenies: str,price: float):
    return "rota converter"
```

3. body paramater.
- Para realizar esse tipo de request será necessário primeiro criar um schema.py informando os tipo de valores que serão passados no body da requisição após ter feito a classe com os atributos basta informa que na rota será passado no body esse tipo de dado. Exxemplo abaixo:
```
@router.get('/async/{from_currency}', response_model=ConverterOutput)
async def async_converter_router(body: ConverterInput,from_currency: str = Path(regex='^[A-Z]{3}$')
):
```

# (Projejto 01)[https://github.com/PedroGuilhermeSilv/API-Convers-o-Moeda]


# (OPrjeto 02)[https://github.com/PedroGuilhermeSilv/Projeto02-FastAPI]