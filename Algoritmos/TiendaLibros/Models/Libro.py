from dataclasses import dataclass
from typing import List
from .Transaccion import Transaccion


@dataclass
class Libro:
    """Modelo para el libro.
    """
    _isbn: str
    _titulo: str
    _cantidad: int
    precio_venta: float
    precion_compra: float
    transaccion: List[Transaccion]

    @property
    def isbn(self):
        return self._isbn

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value: int):
        self._cantidad = value if value >= 0 else self._cantidad
