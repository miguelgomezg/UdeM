from dataclasses import dataclass
from typing import Dict, List
from .Libro import Libro


@dataclass
class Tienda:
    """Modelo para la tienda.
    """
    flujo_caja: float
    catalogo: Dict[str, Libro]
