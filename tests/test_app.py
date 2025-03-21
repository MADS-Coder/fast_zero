from http import HTTPStatus

from fastapi.testclient import TestClient

from src.fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    # Arrange (organização do teste)
    client = TestClient(app)

    # Pega o metodo HTTP GET que encontra-se na aplicação APP.
    # em src/fast_zero/app.py
    # Act (ação)
    response = client.get('/')

    # Usando a instrução assert para avaliar e retornar a condição do teste.
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'mensagem': 'Olá Mundo!'}
