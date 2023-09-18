# Gerenciador de Despesas #

A aplicação que desenvolvi é um Gerenciador de Despesas. A motivação por trás desse projeto surgiu de uma necessidade pessoal, que é a dificuldade em rastrear e controlar meus gastos quando utilizo dinheiro em espécie. Com o uso desse sistema, agora posso acompanhar com precisão o montante total gasto e detalhar as despesas específicas realizadas com dinheiro em espécie.

## Como executar o projeto? ##

Pré requisitos:
- Python 3

#### 1. Abra o terminal na raiz do projeto
#### 2. Crie um ambiente virtual para instalar as dependências
```
python3 -m venv .venv
```

#### 3. Execute o comando para ativar o ambiente
```
source ./.venv/bin/activate
```

#### 4. Instale as dependências
```
pip install -r requirements.txt
```

#### 5. Execute o comando:
```
flask run --host 0.0.0.0 --port 5000
```

### 6. Acesse o endpoint para visualizar o swagger
```
http://localhost:5000/openapi/swagger#/
```

### 7. O banco de dados será criado e populado automaticamente caso não exista