import pytest
from matematica.Calculadora import soma, sub, multiplicacao, divisao, media_lista_valores

def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    soma(v1, v2)
    assert 12 == soma(v1, v2)

def test_soma_dois_valores_negativos():
    v1 = -5.0
    v2 = -7.0
    soma(v1, v2)
    assert -12 == soma(v1, v2)

def test_soma_dois_valores_positivos_e_negativos():
    v1 = -5.0
    v2 = 7.0
    soma(v1, v2)
    assert 2 == soma(v1, v2)

def test_subtracao_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    sub(v1, v2)
    assert -2 == sub(v1, v2)

def test_subtracao_dois_valores_negativos():
    v1 = -5.0
    v2 = -7.0
    sub(v1, v2)
    assert 2 == sub(v1, v2)

def test_subtracao_dois_valores_positivos_e_negativos():
    v1 = -5.0
    v2 = 7.0
    sub(v1, v2)
    assert -12 == sub(v1, v2)

def test_multiplicacao_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    multiplicacao(v1, v2)
    assert 35 == multiplicacao(v1, v2)

def test_multiplicacao_dois_valores_negativos():
    v1 = -5.0
    v2 = -7.0
    multiplicacao(v1, v2)
    assert 35 == multiplicacao(v1, v2)

def test_multiplicacao_dois_valores_positivos_e_negativos():
    v1 = -5.0
    v2 = 7.0
    multiplicacao(v1, v2)
    assert -35 == multiplicacao(v1, v2)

def test_divisao_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    divisao(v1, v2)
    assert 0.7142857142857143 == divisao(v1, v2)

def test_divisao_dois_valores_negativos():
    v1 = -5.0
    v2 = -7.0
    divisao(v1, v2)
    assert 0.7142857142857143 == divisao(v1, v2)

def test_divisao_dois_valores_positivos_e_negativos():
    v1 = -5.0
    v2 = 7.0
    divisao(v1, v2)
    assert -0.7142857142857143 == divisao(v1, v2)

def test_media_lista_valores_positivos():
    v = [1, 2, 3, 4, 5]
    media_lista_valores(v)
    assert 3 == media_lista_valores(v)

def test_media_lista_valores_negativos():
    v = [-1, -2, -3, -4, -5]
    media_lista_valores(v)
    assert -3 == media_lista_valores(v)