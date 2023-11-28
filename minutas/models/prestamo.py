from typing import Optional
from typing import Text

class Prestamo:
    cantidad_banco_a_hipotecante: Optional[Text]
    cantidad_dada_a_aceptante: Optional[Text]
    gastos_de_gestion: Optional[Text]

    def __init__(
        self,
        cantidad_banco_a_hipotecante: int,
        cantidad_dada_a_aceptante: int,
        gastos_de_gestion: int
    ):
        self.cantidad_banco_a_hipotecante = cantidad_banco_a_hipotecante
        self.cantidad_dada_a_aceptante = cantidad_dada_a_aceptante
        self.gastos_de_gestion = gastos_de_gestion