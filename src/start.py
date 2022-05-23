# from domain.entity.User import User
# from domain.entity.Profile import Profile
from domain.entity import Profile, User

perfil = Profile("Admin", "admin@gmail.com")

usuario = User("Giocc", "gioconded@gmail.com")
usuario.name = "Teste"
print(usuario.name)


def soma(a: int, b: int) -> int:
    """Retorna a soma de dois valores.

    Args:
        a (int): Valor 1
        b (int): Valor 2

    Returns:
        int: Resultado da soma
    """
    return a + b


def sub(a: int, b: int) -> int:
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
