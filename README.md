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

    id (chave primária)<br/>
    name<br/>
    user_name (único)<br/>
    password<br/>

## Status <a name="status"></a>
**Colunas**<br/>

    id (chave primária)<br/>
    id_user (chave extrangeira)<br/>
    name<br/>

## Tags <a name="tags"></a>
**Colunas**<br/>

    id (chave primária)<br/>
    id_user (chave extrangeira)<br/>
    name<br/>

## To Do <a name="to-do"></a>
**Colunas**<br/>

    id (chave primária)<br/>
    id_user (chave extrangeira)<br/>
    id_status (chave extrangeira)<br/>
    name<br/>
    description (optional)<br/>
    due date (optional)<br/>

## To Do Tags <a name="to-do-tags"></a>
**Colunas**<br/>

    id (chave primária)<br/>
    id_to_do (chave extrangeira)<br/>
    id_tag (chave extrangeira)<br/>