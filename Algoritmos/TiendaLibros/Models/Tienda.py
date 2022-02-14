from dataclasses import dataclass
from typing import Dict, List
from .Libro import Libro


@dataclass
class Tienda:
    """Modelo para la tienda.
    """
    flujo_caja: float
    catalogo: Dict[str, Libro]

    def registrar_libro(self, libro: Libro):
        if libro.isbn not in self.catalogo.keys():
            self.catalogo[libro.isbn] = libro
        else:
            raise Exception("El libro ya existe en el catalogo")
