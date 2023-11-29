from typing import Type, Text

class Banco:
    nombre: Type[Text]
    nit: Type[Text]

    def __init__(
        self,
        nombre: str,
        nit: str,
    ):
        self.nombre = nombre
        self.nit = nit