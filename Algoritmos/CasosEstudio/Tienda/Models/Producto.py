from dataclasses import dataclass
from enum import Enum


class TipoProducto(Enum):
    DROGUERIA = 1
    PAPELERIA = 2
    SUPER_MERCADO = 3


@dataclass
class Producto:
    nombre: str
    tipo: TipoProducto
    cantidad_actual: int
    cantidad_minima: int
    precio_base: float
    precio_final: float
    vendidos: int
