To Do API
=========
Sumário
-------
1. [Como Usar](#how-to)
2. [Tabelas](#tables)
    1. [User](#user)
    2. [Status](#status)
    3. [Tags](#tags)
    4. [To Do](#to-do)
    5. [To Do Tags](#to-do-tags)

# Como usar <a name="how-to"></a>

Clone o repositório<br/>
Instale as dependências com o comando <br/>
```bash
pip install -r requirements.txt
```
Execute a aplicação
```bash
python app.py
```
Navegue até a url http://localhost:5000/docs em seu browser para acessar o swagger e testar os end-points

# Tabelas <a name="tables"></a>
## User <a name="user"></a>
**Colunas**<br/>

    id (chave primária)
    name
    user_name (único)
    password

## Status <a name="status"></a>
**Colunas**<br/>

    id (chave primária)
    id_user (chave extrangeira)
    name

## Tags <a name="tags"></a>
**Colunas**<br/>

    id (chave primária)
    id_user (chave extrangeira)
    name

## To Do <a name="to-do"></a>
**Colunas**<br/>

    id (chave primária)
    id_user (chave extrangeira)
    id_status (chave extrangeira)
    name
    description (optional)
    due date (optional)

## To Do Tags <a name="to-do-tags"></a>
**Colunas**<br/>

    id (chave primária)
    id_to_do (chave extrangeira)
    id_tag (chave extrangeira)