from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class TipoTransaccion(Enum):
    """
        Constantes para el tipo de transacción.
    """
    COMPRA = 1
    VENTA = 2


@dataclass
class Transaccion:
    """Modelo para la transacción.
    """
    Cantidad: int
    Tipo: TipoTransaccion
    Fecha: datetime = datetime.now()
