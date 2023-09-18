## Como executar o projeto? ##

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