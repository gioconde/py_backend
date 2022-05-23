class Profile:
    """Profile Class."""

    def __init__(self, name, email):
        """Construtor Profile.

        Args:
            name (string): Nome do perfil
            email (Email): Email do perfil
        """
        self.name = name
        self.email = email

    @property
    def name(self):
        """Getter.

        Returns:
            String: Nome do perfil
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
        """Representação de Profile."""
        return f"Nome:{self.__name} Email:{self.email}"
