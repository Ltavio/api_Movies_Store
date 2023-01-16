# API MovieStore

## Descrição:

Nesse projeto foi desenvolvido uma aplicação para gerenciamento de usuários e filmes, além da compra dos filmes, incluindo autenticação e permissões de rotas que diferencia os tipos de usuários logados.

## Tecnologias utilizadas:

- python (ipython)
- django
- djangorestframework
- djangorestframework-simplejwt
- ipdb
- black
- jedi
- pytest
- pytest-django
- pytest-testdox
- PyJWT
- sqlparse


## Endpoints do serviço:

<table>
    <thead>
        <tr>
            <th>Método</th>
            <th>Endpoint</th>
            <th>Objetivo</th>
            <th>Permissão</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>POST</td>
            <td>api/users/</td>
            <td>Criação de usuário</td>
            <td>Livre para acesso</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>users/int:user_id/</td>
            <td>List perfil do usuário</td>
            <td>Somente autenticado</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>api/users/login/</td>
            <td>Autenticar as credenciais de um usuário e retornar um token de acesso JWT.</td>
            <td>Livre para acesso</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>api/movies/</td>
            <td>List movies armazenados</td>
            <td>Livre para acesso</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>api/movies/</td>
            <td>Cadastrar movie</td>
            <td>Somente usuários na categoria employee</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>api/movies/int:movie_id/</td>
            <td>List movie especifico</td>
            <td>Livre para acesso</td>
        </tr>
        <tr>
            <td>DELETE</td>
            <td>api/movies/int:movie_id/</td>
            <td>Deletar movie</td>
            <td>Somente usuários na categoria employee</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>api/movies/int:movie_id/orders/</td>
            <td>Comprar movie</td>
            <td>Somente autenticado</td>
        </tr>
    </tbody>
</table>

### Para inicializar a aplicação:
````
python manage.py runserver
````

- Rodando os testes:
```
pytest --testdox -vvs
```
