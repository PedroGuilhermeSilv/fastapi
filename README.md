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

## Alembic
- O alembic será um pluguin responsávbel por nossas migracões para o banco de dados, os comandos mais utilizados são:
```
alembic init
```
- Após nicilaizar temos que configurar o `env.py` e o `alembic.init` para peguerem das variáveis de ambiente o caminho do banco de dados. Logo após podemos criar um scprit de migration com o comando:
```
alembic revision --autogenerate -m "add categories table"
```
- Após criar o scprit, podemos executá-lo com o comando:
``` 
alembic upgrade head
```

## Seção 7: Segurança e Autenticação (Continuação Projeto 2)

## Seção 8: Paginação (Continuação Projeto 2)
- Para adicionar a paginação na sua rota precisaremos de uma lib chamada de `fastapi_pagination`. Instalada a dependência teremos agrupar em nossa rota.
1. O response model da rota deve ser `Page[]`
2. O return da rota deve ser `paginate`
3. adicionar a rota pela função `add_pagination()`

```

@router.get('/list', response_model=Page[CategoryOutput])
def list_categories():
    categories = [
        CategoryOutput(name=f'category {n}', slug=f'category-{n}',id=n)
        for n in range(100)
    ]
    return paginate(categories)
add_pagination(router)

```

# (Projejto 01)[https://github.com/PedroGuilhermeSilv/API-Convers-o-Moeda]


# (OPrjeto 02)[https://github.com/PedroGuilhermeSilv/Projeto02-FastAPI]