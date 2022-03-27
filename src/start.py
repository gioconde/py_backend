from .domain.entity import User


usuario = User("Gi", "gioconded@gmail.com")
usuario.name = "Teste"
print(usuario.name)


def soma(a, b):
    """Retorna a soma de dois valores.

    Args:
        a (int): Valor 1
        b (int): Valor 2

    Returns:
        int: Resultado da soma
    """
    return a + b


def sub(a, b):
    """Retorna a subtração de dois valores.

    Args:
        a (int): Valor 1
        b (int): Valor 2

    Returns:
        int: Resultado da subtração
    """
    return a - b


CONSTANTE = sub(soma(2, 4), 1)
print(CONSTANTE)
