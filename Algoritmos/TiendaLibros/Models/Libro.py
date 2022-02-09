from dataclasses import dataclass
from typing import List
from xmlrpc.client import DateTime

from .Transaccion import Transaccion


@dataclass
class Libro:
    titulo: str
    cantidad: int
    precio_venta : float
    precion_compra: float
    transaccion : List[Transaccion]
    fecha_publicacion : DateTime
    