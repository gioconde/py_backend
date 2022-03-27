class User:
    """User Class."""

    def __init__(self, name, email):
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
        return self.__name

    @name.setter
    def name(self, name):
        name_size = 2
        if len(name) < name_size:
            message = "Nome deve ter pelo menos "
            +f"{name_size} caracteres."
            raise Exception(message)
        self.__name = name

    @name.getter
    def name(self):
        return self.__name + " getter."

    def __str__(self):
        """Representação de User."""
        return f"Nome:{self.__name} Email:{self.email}"
