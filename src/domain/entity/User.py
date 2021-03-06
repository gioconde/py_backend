class User:
    """User Class."""

    def __init__(self, name: str, email):
        """Construtor User.

        Args:
            name (string): Nome do usuário
            email (Email): Email do usuário
        """
        self.name = name
        self.email = email

    @property
    def name(self):
        """Getter.

        Returns:
            String: Nome do usuário
        """
        return self.__name + " getter."

    @name.setter
    def name(self, name):
        name_size = 2
        if len(name) < name_size:
            message = (
                "Adicionando caracteres para aumentar o tamanho do texto."
                + " Nome deve ter pelo menos "
                + f"{name_size} caracteres."
            )
            raise Exception(message)
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

    def __str__(self):
        """Representação de User."""
        return f"Nome:{self.__name} Email:{self.email}"
