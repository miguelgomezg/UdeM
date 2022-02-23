from dataclasses import dataclass
from typing import List
from .Producto import Producto


@dataclass
class Tienda:
    productos: List[Producto]
