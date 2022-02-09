from dataclasses import dataclass
from typing import List
from Models.Libro import Libro


@dataclass
class Tienda:
    flujo_caja: float
    catalogo: List[Libro]