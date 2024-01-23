import sys

sys.path.append('..')
from src.controller import cliente


def test_concatenacao_nome_sobrenome():
    p1 = cliente.Pessoa('Fernanda', 'Maia', 58, '88845990168')
    assert p1.nome_completo() == 'Fernanda Maia'
